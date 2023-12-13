from .tsl_parser import TSLParser
from typing import List

class DependencyVisualizer:
    """
    Visualizes dependencies between test cases in a TSL script.
    """

    def __init__(self, tsl_parser: TSLParser):
        self.tsl_parser: TSLParser = tsl_parser

    def visualize(self) -> str:
        """
        Creates a string representation of the dependencies between test cases.
        """
        dependency_graph: str = "graph TD\n"
        test_cases: List[str] = self.tsl_parser.extract_test_cases()
    
        for i in range(1, len(test_cases)):
            dependency_graph += f"  {test_cases[i-1]} --> {test_cases[i]}\n"
    
        return dependency_graph
