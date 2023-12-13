import pytest
from src.tsl_parser import TSLParser
from src.dependency_visualizer import DependencyVisualizer

def test_visualize_empty():
    parser = TSLParser("")
    visualizer = DependencyVisualizer(parser)
    assert visualizer.visualize() == "graph TD\n"

def test_visualize_single_case():
    tsl_script = "Test Case: TC1"
    parser = TSLParser(tsl_script)
    visualizer = DependencyVisualizer(parser)
    assert visualizer.visualize() == "graph TD\n"

def test_visualize_multiple_cases():
    tsl_script = "Test Case: TC1\nTest Case: TC2"
    parser = TSLParser(tsl_script)
    visualizer = DependencyVisualizer(parser)
    expected_output = "graph TD\n  TC1 --> TC2\n"
    assert visualizer.visualize() == expected_output

def test_visualize_no_cases():
    tsl_script = "Test Scenario: Scenario"
    parser = TSLParser(tsl_script)
    visualizer = DependencyVisualizer(parser)
    assert visualizer.visualize() == "graph TD\n"

# Test for unstructured text in the script
def test_visualize_unstructured_text():
    tsl_script = "This is not a valid TSL script."
    parser = TSLParser(tsl_script)
    visualizer = DependencyVisualizer(parser)
    assert visualizer.visualize() == "graph TD\n"
