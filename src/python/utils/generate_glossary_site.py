"""
Generate a static, linkable glossary website from a SKOS glossary.

The page follows the glossary page pattern of the design system of the Swiss
federal administration (https://swiss.github.io/designsystem/, "Pages/Glossar"):
sticky search, letter badge filter, filter drawer, sorting, entry count,
letter titles and accordion entries. Every entry can be linked with
"<page>#<local name of the concept IRI>".

Besides the glossary, the ontology and the SHACL shapes are read to show which
business object of the logical data model is defined by a glossary term
(rdfs:isDefinedBy).
"""

import argparse
import html
import json
import shutil
import unicodedata
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import OWL, SH, SKOS

SCHEMA = Namespace("http://schema.org/")
LANG = "de"
LANGUAGE_NAMES = {"fr": "Französisch", "it": "Italienisch", "rm": "Rätoromanisch", "en": "Englisch"}


def literal(g, subject, predicate, lang=LANG):
    """Returns the literal in the requested language, falling back to untagged literals."""
    fallback = None
    for obj in g.objects(subject, predicate):
        obj_lang = getattr(obj, "language", None)
        if obj_lang == lang:
            return str(obj)
        if obj_lang is None:
            fallback = str(obj)
    return fallback


def literals(g, subject, predicate):
    return sorted((str(o), getattr(o, "language", None)) for o in g.objects(subject, predicate))


def local_name(iri):
    return str(iri).rstrip("/").rsplit("/", 1)[-1]


def sort_key(text):
    """German collation approximation: umlauts sort like their base letters."""
    normalized = unicodedata.normalize("NFKD", text.lower())
    return "".join(c for c in normalized if not unicodedata.combining(c))


def letter_of(text):
    first = sort_key(text)[:1]
    if first.isdigit():
        return "0-9"
    return first if first.isalpha() else "0-9"


def qname(g, iri):
    try:
        return g.namespace_manager.normalizeUri(iri)
    except Exception:
        return str(iri)


def collect_entries(glossary, model):
    concepts = set(glossary.subjects(RDF.type, SKOS.Concept))
    names = {c: literal(glossary, c, SCHEMA.name) or local_name(c) for c in concepts}

    narrower = {c: [] for c in concepts}
    for child, parent in glossary.subject_objects(SKOS.broader):
        if parent in narrower:
            narrower[parent].append(child)

    collections = {}
    for coll in glossary.subjects(RDF.type, SKOS.Collection):
        collections[coll] = literal(glossary, coll, SCHEMA.name) or local_name(coll)
    membership = {c: [] for c in concepts}
    for coll, member in glossary.subject_objects(SKOS.member):
        if member in membership and coll in collections:
            membership[member].append(local_name(coll))

    business_objects = {c: [] for c in concepts}
    for resource, term in model.subject_objects(RDFS.isDefinedBy):
        if term not in business_objects:
            continue
        kind = "Klasse" if (resource, RDF.type, OWL.Class) in model else "Merkmal"
        label = literal(model, resource, RDFS.label) or local_name(resource)
        business_objects[term].append({
            "qname": qname(model, resource),
            "label": label,
            "kind": kind,
            # Same slug as in generate_shacl_docs.py
            "anchor": "sec-nodeshape-" + local_name(resource).lower() if (resource, RDF.type, SH.NodeShape) in model else None,
        })

    def ref(c):
        return {"id": local_name(c), "name": names[c]}

    entries = []
    for c in concepts:
        name = names[c]
        other_languages = sorted(
            ({"lang": lang, "language": LANGUAGE_NAMES.get(lang, lang), "name": value}
             for value, lang in literals(glossary, c, SCHEMA.name) if lang and lang != LANG),
            key=lambda o: list(LANGUAGE_NAMES).index(o["lang"]) if o["lang"] in LANGUAGE_NAMES else len(LANGUAGE_NAMES),
        )
        citations = []
        for obj in glossary.objects(c, SCHEMA.citation):
            if isinstance(obj, URIRef):
                citations.append({"href": str(obj), "text": str(obj)})
            else:
                citations.append({"href": None, "text": str(obj)})
        entries.append({
            "id": local_name(c),
            "iri": str(c),
            "name": name,
            "letter": letter_of(name),
            "sort": sort_key(name),
            "alternateNames": [v for v, lang in literals(glossary, c, SCHEMA.alternateName) if lang in (LANG, None)],
            "otherLanguages": other_languages,
            "description": literal(glossary, c, SCHEMA.description) or "",
            "scopeNote": literal(glossary, c, SKOS.scopeNote) or "",
            "broader": sorted((ref(b) for b in glossary.objects(c, SKOS.broader) if b in names), key=lambda r: sort_key(r["name"])),
            "narrower": sorted((ref(n) for n in narrower[c]), key=lambda r: sort_key(r["name"])),
            "related": sorted((ref(r) for r in glossary.objects(c, SKOS.related) if r in names), key=lambda r: sort_key(r["name"])),
            "citations": sorted(citations, key=lambda x: x["text"]),
            "collections": sorted(membership[c]),
            "businessObjects": sorted(business_objects[c], key=lambda b: (b["kind"], b["qname"])),
        })
    entries.sort(key=lambda e: e["sort"])
    collection_list = sorted(
        ({"id": local_name(k), "name": v} for k, v in collections.items()),
        key=lambda x: sort_key(x["name"]),
    )
    return entries, collection_list


def esc(text):
    return html.escape(text or "", quote=True)


def render_entry(e, doc_url):
    parts = [f'<p class="glossary-entry__definition">{esc(e["description"])}</p>']

    facts = []
    if e["alternateNames"]:
        facts.append(("Synonyme und Abkürzungen", ", ".join(esc(a) for a in e["alternateNames"])))
    if e["otherLanguages"]:
        facts.append(("Andere Sprachen", "; ".join(
            f'<span lang="{esc(o["lang"])}">{esc(o["name"])}</span> <span class="text--secondary">({esc(o["language"])})</span>'
            for o in e["otherLanguages"])))

    def links(refs):
        return ", ".join(f'<a href="#{esc(r["id"])}" data-term-link="{esc(r["id"])}">{esc(r["name"])}</a>' for r in refs)

    if e["broader"]:
        facts.append(("Oberbegriff", links(e["broader"])))
    if e["narrower"]:
        facts.append(("Unterbegriffe", links(e["narrower"])))
    if e["related"]:
        facts.append(("Verwandte Begriffe", links(e["related"])))
    if e["businessObjects"]:
        items = []
        for b in e["businessObjects"]:
            label = f'<code>{esc(b["qname"])}</code> {esc(b["label"])} <span class="text--secondary">({esc(b["kind"])})</span>'
            if b["anchor"] and doc_url:
                label = f'<a href="{esc(doc_url)}#{esc(b["anchor"])}">{label}</a>'
            items.append(label)
        facts.append(("Im Datenmodell", "<br>".join(items)))
    if e["citations"]:
        cites = []
        for c in e["citations"]:
            if c["href"]:
                cites.append(f'<a href="{esc(c["href"])}" rel="noopener" target="_blank">{esc(c["text"])}</a>')
            else:
                cites.append(esc(c["text"]))
        facts.append(("Quelle", "<br>".join(cites)))

    if e["scopeNote"]:
        parts.append(f'<div class="glossary-entry__note"><strong>Anmerkung</strong><p>{esc(e["scopeNote"])}</p></div>')
    if facts:
        rows = "".join(f"<dt>{label}</dt><dd>{value}</dd>" for label, value in facts)
        parts.append(f'<dl class="glossary-entry__facts">{rows}</dl>')
    parts.append(
        '<div class="glossary-entry__meta">'
        f'<span class="text--secondary">IRI</span> <a class="glossary-entry__iri" href="{esc(e["iri"])}">{esc(e["iri"])}</a>'
        f'<button type="button" class="btn btn--outline btn--sm" data-copy-link="{esc(e["id"])}">Link kopieren</button>'
        "</div>"
    )
    return "".join(parts)


def render_page(entries, collections, meta, template):
    letters = ["0-9"] + [chr(c) for c in range(ord("a"), ord("z") + 1)]
    used = {e["letter"] for e in entries}
    badges = ['<button type="button" class="badge badge--negative" data-letter="all" aria-pressed="true">Alle</button>']
    for letter in letters:
        disabled = "" if letter in used else ' disabled aria-disabled="true"'
        badges.append(f'<button type="button" class="badge badge--gray" data-letter="{letter}" aria-pressed="false"{disabled}>{letter.upper()}</button>')

    # Group entries by their first letter, like GlossarResultList of the design system
    groups = {}
    for e in entries:
        search_text = " ".join([e["name"], e["description"], e["scopeNote"], *e["alternateNames"], *(o["name"] for o in e["otherLanguages"])])
        groups.setdefault(e["letter"], []).append(
            f'<details class="accordion__item" id="{esc(e["id"])}" data-letter="{esc(e["letter"])}" '
            f'data-sort="{esc(e["sort"])}" data-collections="{esc(" ".join(e["collections"]))}" '
            f'data-model="{"yes" if e["businessObjects"] else "no"}" data-search="{esc(search_text.lower())}">'
            f'<summary class="accordion__button"><h3 class="accordion__title">{esc(e["name"])}</h3>'
            '<svg class="accordion__arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M5.3 8.3 12 15l6.7-6.7 1.4 1.4L12 17.8 3.9 9.7z"/></svg>'
            f'</summary><div class="accordion__content">{render_entry(e, meta["doc_url"])}</div></details>'
        )
    items = [
        f'<section class="glossar-result__group" data-group="{esc(letter)}">'
        f'<h2 class="glossar-result__title">{esc(letter.upper())}</h2>'
        f'<div class="accordion">{"".join(group)}</div></section>'
        for letter, group in sorted(groups.items(), key=lambda kv: ("" if kv[0] == "0-9" else kv[0]))
    ]

    options = "".join(f'<option value="{esc(c["id"])}">{esc(c["name"])}</option>' for c in collections)
    replacements = {
        "{{TITLE}}": esc(meta["title"]),
        "{{DESCRIPTION}}": esc(meta["description"]),
        "{{VERSION}}": esc(meta["version"]),
        "{{MODIFIED}}": esc(meta["modified"]),
        "{{COUNT}}": str(len(entries)),
        "{{BADGES}}": "".join(badges),
        "{{COLLECTION_OPTIONS}}": options,
        "{{ENTRIES}}": "".join(items),
        "{{FLAG_SVG}}": meta["flag_svg"],
        "{{WORDMARK_SVG}}": meta["wordmark_svg"],
        "{{DOC_URL}}": esc(meta["doc_url"]),
        "{{REPO_URL}}": esc(meta["repo_url"]),
        "{{JSON_LD}}": json.dumps(meta["json_ld"], ensure_ascii=False).replace("</", "<\\/"),
    }
    page = template
    for key, value in replacements.items():
        page = page.replace(key, value)
    return page


def main():
    parser = argparse.ArgumentParser(description="Generate a glossary website in the style of the Swiss federal design system.")
    parser.add_argument("-i", "--input", required=True, help="SKOS glossary (.ttl)")
    parser.add_argument("-m", "--model", nargs="*", default=[], help="Ontology and shape files (.ttl) of the data model")
    parser.add_argument("-p", "--prefixes", help="Prefix file (.ttl) to shorten IRIs")
    parser.add_argument("-t", "--template", required=True, help="HTML template of the glossary page")
    parser.add_argument("-a", "--assets", required=True, help="Directory containing flag.svg and wordmark.svg")
    parser.add_argument("-o", "--output", required=True, help="Output directory of the glossary website")
    parser.add_argument("--doc-url", default="../de/index.html", help="URL of the standard's documentation")
    parser.add_argument("--repo-url", default="https://github.com/blw-ofag-ufag/eCH-0264")
    args = parser.parse_args()

    glossary = Graph().parse(args.input, format="turtle")
    model = Graph(bind_namespaces="none")
    for path in args.model:
        model.parse(path, format="turtle")
    if args.prefixes:
        prefixes = Graph(bind_namespaces="none").parse(args.prefixes, format="turtle")
        for prefix, uri in prefixes.namespaces():
            model.bind(str(prefix), uri, override=True, replace=True)

    scheme = next(glossary.subjects(RDF.type, SKOS.ConceptScheme))
    entries, collections = collect_entries(glossary, model)

    assets = Path(args.assets)
    meta = {
        "title": literal(glossary, scheme, SCHEMA.name) or "Glossar",
        "description": literal(glossary, scheme, SCHEMA.description) or "",
        "version": literal(glossary, scheme, SCHEMA.version) or "",
        "modified": literal(glossary, scheme, SCHEMA.dateModified) or "",
        "doc_url": args.doc_url,
        "repo_url": args.repo_url,
        "flag_svg": (assets / "flag.svg").read_text(encoding="utf-8").strip(),
        "wordmark_svg": (assets / "wordmark.svg").read_text(encoding="utf-8").strip(),
        "json_ld": {
            "@context": "https://schema.org",
            "@type": "DefinedTermSet",
            "@id": str(scheme),
            "name": literal(glossary, scheme, SCHEMA.name),
            "hasDefinedTerm": [
                {"@type": "DefinedTerm", "@id": e["iri"], "name": e["name"], "description": e["description"], "url": "#" + e["id"]}
                for e in entries
            ],
        },
    }

    template = Path(args.template).read_text(encoding="utf-8")
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(render_page(entries, collections, meta, template), encoding="utf-8")
    shutil.copyfile(args.input, out / "glossary.skos.ttl")
    print(f"Glossary website with {len(entries)} entries written to {out / 'index.html'}")


if __name__ == "__main__":
    main()
