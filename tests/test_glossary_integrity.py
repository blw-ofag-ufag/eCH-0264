import pytest
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS
from rdflib.namespace import SKOS

SCHEMA = Namespace("http://schema.org/")

GLOSSARY_PATH = Path("src/rdf/data/glossary.skos.ttl")
ONTOLOGY_PATH = Path("src/rdf/ontology/model.owl.ttl")


@pytest.fixture(scope="module")
def glossary():
    if not GLOSSARY_PATH.exists():
        pytest.skip(f"Glossary not found: {GLOSSARY_PATH}")
    return Graph().parse(GLOSSARY_PATH, format="turtle")


def concepts(g):
    return set(g.subjects(RDF.type, SKOS.Concept))


def ancestors(g, concept):
    seen = set()
    stack = list(g.objects(concept, SKOS.broader))
    while stack:
        c = stack.pop()
        if c not in seen:
            seen.add(c)
            stack.extend(g.objects(c, SKOS.broader))
    return seen


def test_no_cycles_in_hierarchy(glossary):
    """skos:broader must not form cycles."""
    cyclic = [c for c in concepts(glossary) if c in ancestors(glossary, c)]
    assert not cyclic, f"Cyclic skos:broader hierarchy for: {sorted(map(str, cyclic))}"


def test_related_is_disjoint_with_broader_transitive(glossary):
    """SKOS integrity condition S27: skos:related is disjoint with skos:broaderTransitive."""
    errors = []
    for s, o in glossary.subject_objects(SKOS.related):
        if o in ancestors(glossary, s) or s in ancestors(glossary, o):
            errors.append(f"{s} skos:related {o}")
    assert not errors, "Related concepts must not be hierarchically linked:\n" + "\n".join(errors)


def test_related_targets_exist(glossary):
    """All skos:broader and skos:related targets must be defined in the glossary."""
    defined = concepts(glossary)
    missing = [
        f"{s} -> {o}"
        for p in (SKOS.broader, SKOS.related)
        for s, o in glossary.subject_objects(p)
        if o not in defined
    ]
    assert not missing, "Undefined targets:\n" + "\n".join(missing)


def test_unique_german_names(glossary):
    """Two concepts must not share the same German preferred name."""
    names = {}
    for c in concepts(glossary):
        for name in glossary.objects(c, SCHEMA.name):
            if getattr(name, "language", None) == "de":
                names.setdefault(str(name).lower(), []).append(str(c))
    duplicates = {n: cs for n, cs in names.items() if len(cs) > 1}
    assert not duplicates, f"Duplicate German names: {duplicates}"


def test_every_concept_has_a_german_definition(glossary):
    """Every glossary entry must have a German definition (schema:description)."""
    missing = [
        str(c) for c in concepts(glossary)
        if not any(getattr(d, "language", None) == "de" for d in glossary.objects(c, SCHEMA.description))
    ]
    assert not missing, f"Concepts without German definition: {sorted(missing)}"


def test_every_concept_is_in_a_collection(glossary):
    """Every concept must be a member of at least one thematic skos:Collection."""
    members = set(glossary.objects(None, SKOS.member))
    missing = concepts(glossary) - members
    assert not missing, f"Concepts not in any collection: {sorted(map(str, missing))}"


def test_collection_members_exist(glossary):
    """Collections must only reference concepts defined in the glossary."""
    unknown = set(glossary.objects(None, SKOS.member)) - concepts(glossary)
    assert not unknown, f"Collections reference unknown concepts: {sorted(map(str, unknown))}"


def test_model_is_defined_by_glossary(glossary):
    """Every rdfs:isDefinedBy of the ontology must point to a glossary concept."""
    if not ONTOLOGY_PATH.exists():
        pytest.skip(f"Ontology not found: {ONTOLOGY_PATH}")
    ontology = Graph().parse(ONTOLOGY_PATH, format="turtle")
    missing = [
        f"{s} -> {o}" for s, o in ontology.subject_objects(RDFS.isDefinedBy)
        if o not in concepts(glossary)
    ]
    assert not missing, "Ontology references undefined glossary terms:\n" + "\n".join(missing)
