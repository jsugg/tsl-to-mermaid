"""
Module: Mermaid Converter
Description: Converts TSL script content to Mermaid diagram format.
"""

from typing import List
from .tsl_parser import TSLParser
import re

class MermaidConverter:
    """Class to convert TSL scripts into Mermaid diagram format."""
    
    def __init__(self, tsl_parser: TSLParser):
        self.tsl_parser: TSLParser = tsl_parser

    def convert(self, output_format: str) -> str:
        """Converts the TSL script to the specified output format ('mermaid' or 'comments')."""
        if output_format == "mermaid":
            return self._to_mermaid()
        elif output_format == "comments":
            return "\n".join(self.tsl_parser.extract_comments())
        else:
            return "Invalid output format. Use 'mermaid' or 'comments'."

    def _to_mermaid(self) -> str:
        """Private method to convert the TSL script into Mermaid format."""
        mermaid_code: str = "graph TD\n"
        scenarios: List[str] = self.tsl_parser.extract_scenarios()
        test_cases: List[str] = self.tsl_parser.extract_test_cases()

        for scenario in scenarios:
            mermaid_code += f"  {scenario}[{scenario}]\n"
            for test_case in test_cases:
                mermaid_code += f"  {scenario} --> {test_case}[{test_case}]\n"
                mermaid_code += self._extract_test_case_details(test_case)

        return mermaid_code

    def _extract_test_case_details(self, test_case: str) -> str:
        """Extracts and formats the details of a specific test case."""
        details: str = ""
        test_case_section = re.search(rf"Test Case: {test_case}.*?(?=Test Case:|$)", self.tsl_parser.tsl_script, re.DOTALL)
        if test_case_section:
            test_case_content: str = test_case_section.group()
            for line in test_case_content.split('\n'):
                if line.strip() and not line.startswith('Test Case:'):
                    details += f"  {test_case} --> \"{line.strip()}\"\n"
        return details
