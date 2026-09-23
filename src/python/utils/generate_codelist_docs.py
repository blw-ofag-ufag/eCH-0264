"""
Generate Markdown documentation for all code lists (skos:ConceptScheme) of the
data model, except the glossary itself.
"""

import argparse
import re
from pathlib import Path

from rdflib import Graph, Namespace, RDF
from rdflib.namespace import SKOS

SCHEMA = Namespace("http://schema.org/")

TRANSLATIONS = {
    "de": {"code": "Code", "name": "Wert", "desc": "Beschreibung", "iri": "IRI", "list": "Codeliste"},
    "fr": {"code": "Code", "name": "Valeur", "desc": "Description", "iri": "IRI", "list": "Liste de codes"},
    "it": {"code": "Codice", "name": "Valore", "desc": "Descrizione", "iri": "IRI", "list": "Lista di codici"},
    "en": {"code": "Code", "name": "Value", "desc": "Description", "iri": "IRI", "list": "Code list"},
}


def localized(g, subject, predicate, lang):
    values = {getattr(o, "language", None): str(o) for o in g.objects(subject, predicate)}
    return values.get(lang) or values.get("de") or values.get(None) or ""


def cell(text):
    return re.sub(r"\s+", " ", text or "").replace("|", "\\|").strip()


def depth(g, concept):
    d = 0
    while (concept := next(g.objects(concept, SKOS.broader), None)) is not None:
        d += 1
    return d


def ordered_concepts(g, scheme):
    concepts = list(g.subjects(SKOS.inScheme, scheme))
    children = {c: [] for c in concepts}
    roots = []
    for c in concepts:
        parent = next(g.objects(c, SKOS.broader), None)
        (children[parent] if parent in children else roots).append(c)
    ordered = []

    def visit(nodes):
        # Sort by code if present, else by the German name
        for node in sorted(nodes, key=lambda n: (str(next(g.objects(n, SCHEMA.identifier), "")), localized(g, n, SCHEMA.name, "de").lower())):
            ordered.append(node)
            visit(children[node])

    visit(roots)
    return ordered


def main():
    parser = argparse.ArgumentParser(description="Generate Markdown documentation of SKOS code lists.")
    parser.add_argument("-i", "--input", required=True, help="Code list file (.ttl)")
    parser.add_argument("-d", "--docs_dir", required=True, help="Docs directory containing language subdirectories")
    parser.add_argument("-p", "--prefixes", help="Prefix file (.ttl) to shorten IRIs")
    args = parser.parse_args()

    g = Graph(bind_namespaces="none")
    g.parse(args.input, format="turtle")
    if args.prefixes:
        prefixes = Graph(bind_namespaces="none").parse(args.prefixes, format="turtle")
        for prefix, uri in prefixes.namespaces():
            g.bind(str(prefix), uri, override=True, replace=True)

    docs_dir = Path(args.docs_dir)
    schemes = sorted(g.subjects(RDF.type, SKOS.ConceptScheme), key=lambda s: localized(g, s, SCHEMA.name, "de").lower())

    for lang, t in TRANSLATIONS.items():
        if not (docs_dir / lang).is_dir():
            continue
        lines = []
        for scheme in schemes:
            name = localized(g, scheme, SCHEMA.name, lang)
            slug = re.sub(r"[^a-z0-9]+", "-", str(scheme).rstrip("/").split("/")[-2].lower()).strip("-")
            lines.append(f"## {name} {{#sec-codelist-{slug}}}")
            lines.append("")
            description = localized(g, scheme, SCHEMA.description, lang)
            if description:
                lines.append(cell(description))
                lines.append("")
            lines.append(f"**{t['list']}:** `{g.namespace_manager.normalizeUri(scheme)}`")
            lines.append("")
            lines.append(f"| {t['code']} | {t['name']} | {t['desc']} | {t['iri']} |")
            lines.append("|:--|:--|:--|:--|")
            for concept in ordered_concepts(g, scheme):
                code = str(next(g.objects(concept, SCHEMA.identifier), ""))
                indent = "&nbsp;&nbsp;&nbsp;" * depth(g, concept)
                value = indent + cell(localized(g, concept, SCHEMA.name, lang))
                desc = cell(" ".join(filter(None, [
                    localized(g, concept, SCHEMA.description, lang),
                    localized(g, concept, SKOS.scopeNote, lang),
                ])))
                lines.append(f"| {code} | {value} | {desc} | `{g.namespace_manager.normalizeUri(concept)}` |")
            lines.append("")
            lines.append(f": {name} {{#tbl-codelist-{slug}}}")
            lines.append("")
        (docs_dir / lang / "codelists.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
