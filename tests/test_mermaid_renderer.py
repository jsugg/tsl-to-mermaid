import pytest
from src.tsl_parser import TSLParser

# Test extraction of comments from a valid TSL script
def test_extract_comments():
    tsl_script = "# Comment 1\n# Comment 2"
    parser = TSLParser(tsl_script)
    assert parser.extract_comments() == ["# Comment 1", "# Comment 2"]

# Test extraction of scenarios from a valid TSL script
def test_extract_scenarios():
    tsl_script = "Test Scenario: Scenario1\nTest Scenario: Scenario2"
    parser = TSLParser(tsl_script)
    assert parser.extract_scenarios() == ["Scenario1", "Scenario2"]

# Test extraction of test cases from a valid TSL script
def test_extract_test_cases():
    tsl_script = "Test Case: TC1\nTest Case: TC2"
    parser = TSLParser(tsl_script)
    assert parser.extract_test_cases() == ["TC1", "TC2"]

# Test validation of a correctly structured TSL script
def test_is_valid():
    tsl_script = "Test Scenario: Scenario\nTest Case: TC\nDescription: Desc\nPreconditions: Pre\nSteps: Step\nExpected Results: Result"
    parser = TSLParser(tsl_script)
    assert parser.is_valid()

# Test validation of an incorrectly structured TSL script
def test_is_not_valid():
    tsl_script = "Test Case: TC\nDescription: Desc"
    parser = TSLParser(tsl_script)
    assert not parser.is_valid()

# Test parser behavior with empty input
def test_empty_script():
    parser = TSLParser("")
    assert not parser.extract_comments()
    assert not parser.extract_scenarios()
    assert not parser.extract_test_cases()
    assert not parser.is_valid()
