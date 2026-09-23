import pytest
from pathlib import Path
from rdflib import Graph
from pyshacl import validate

EXAMPLE = Path("docs/data/example.ttl")
ONTOLOGY = Path("src/rdf/ontology/model.owl.ttl")
CODELISTS = Path("src/rdf/data/codelists.ttl")
SHAPES = Path("src/rdf/shapes/model.shacl.ttl")


def load(*paths):
    g = Graph()
    for path in paths:
        g.parse(path, format="turtle")
    return g


def test_example_conforms_to_model():
    """The fictitious example in the documentation must conform to the data model."""
    for path in (EXAMPLE, ONTOLOGY, CODELISTS, SHAPES):
        if not path.exists():
            pytest.skip(f"File not found: {path}")

    conforms, _, report = validate(
        load(EXAMPLE, CODELISTS),
        shacl_graph=load(SHAPES),
        ont_graph=load(ONTOLOGY),
        inference="rdfs",
        advanced=True,
    )
    if not conforms:
        pytest.fail(f"docs/data/example.ttl does not conform to the SHACL shapes:\n\n{report}", pytrace=False)


PREFIXES = """
    PREFIX eCH-0264: <https://agriculture.ld.admin.ch/eCH-0264/1/>
    PREFIX example: <https://agriculture.ld.admin.ch/eCH-0264/1/example/>
    PREFIX result: <https://agriculture.ld.admin.ch/eCH-0264/1/result-value/>
"""

INVALID_CASES = {
    "deficiency result without deficiency": """
        DELETE { example:ResultJournal eCH-0264:deficiency ?d } WHERE { example:ResultJournal eCH-0264:deficiency ?d }
    """,
    "result without explicit value": """
        DELETE { example:ResultOutdoor eCH-0264:resultValue ?v } WHERE { example:ResultOutdoor eCH-0264:resultValue ?v }
    """,
    "control point of another rubric": """
        INSERT DATA {
            example:ScopeRAUS eCH-0264:controlPointResult example:ResultLabel .
            example:ResultLabel a eCH-0264:ControlPointResult ;
                eCH-0264:controlPoint example:LabelControlPointOutdoor-2026 ;
                eCH-0264:resultValue result:Compliant .
        }
    """,
    "two results for the same control point": """
        INSERT DATA {
            example:ScopeRAUS eCH-0264:controlPointResult example:ResultOutdoorTwice .
            example:ResultOutdoorTwice a eCH-0264:ControlPointResult ;
                eCH-0264:controlPoint example:ControlPointOutdoor-2026 ;
                eCH-0264:resultValue result:NotInspected .
        }
    """,
}


@pytest.mark.parametrize("case", INVALID_CASES.keys())
def test_invalid_example_is_rejected(case):
    """Modifications that reintroduce implicit or ambiguous results must be rejected."""
    broken = load(EXAMPLE, CODELISTS)
    broken.update(PREFIXES + INVALID_CASES[case])
    conforms, _, _ = validate(
        broken,
        shacl_graph=load(SHAPES),
        ont_graph=load(ONTOLOGY),
        inference="rdfs",
        advanced=True,
    )
    assert not conforms, f"The example must not validate with: {case}"
