import pytest
from src.tsl_parser import TSLParser
from src.mermaid_converter import MermaidConverter

def test_convert_to_mermaid_empty():
    parser = TSLParser("")
    converter = MermaidConverter(parser)
    assert converter.convert("mermaid") == "graph TD\n"

def test_convert_to_comments():
    tsl_script = "# Comment\nTest Case: TC1"
    parser = TSLParser(tsl_script)
    converter = MermaidConverter(parser)
    assert converter.convert("comments") == "# Comment"

def test_invalid_format():
    parser = TSLParser("")
    converter = MermaidConverter(parser)
    assert converter.convert("invalid") == "Invalid output format. Use 'mermaid' or 'comments'."

def test_convert_to_mermaid_with_data():
    tsl_script = "Test Scenario: Scenario1\nTest Case: TC1\nDescription: Description1\nPreconditions: Preconditions1\nSteps: Steps1\nExpected Results: Results1"
    parser = TSLParser(tsl_script)
    converter = MermaidConverter(parser)
    expected_output = "graph TD\n  Scenario1[Scenario1]\n  Scenario1 --> TC1[TC1]\n  TC1 --> \"Description: Description1\"\n  TC1 --> \"Preconditions: Preconditions1\"\n  TC1 --> \"Steps: Steps1\"\n  TC1 --> \"Expected Results: Results1\"\n"
    assert converter.convert("mermaid") == expected_output

# Test for script with missing sections
def test_convert_with_missing_sections():
    tsl_script = "Test Case: TC1\nDescription: Description1"
    parser = TSLParser(tsl_script)
    converter = MermaidConverter(parser)
    expected_output = ("graph TD\n"
                       "  TC1 --> \"Description: Description1\"\n")
    assert converter.convert("mermaid") == expected_output