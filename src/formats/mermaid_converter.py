from typing import List
from .base_converter import BaseConverter
from ..tsl_parser import TSLParser
import re

class MermaidConverter(BaseConverter):
    """
    Converts TSL script content to Mermaid diagram format.
    """

    def __init__(self, tsl_parser: TSLParser):
        self.tsl_parser: TSLParser = tsl_parser

    def convert(self) -> str:
        """
        Converts the TSL script to Mermaid diagram format.
        """
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
        """
        Extracts detailed information for a specific test case.
        """
        details: str = ""
        test_case_section = re.search(rf"Test Case: {test_case}.*?(?=Test Case:|$)", self.tsl_parser.tsl_script, re.DOTALL)
        if test_case_section:
            test_case_content: str = test_case_section.group()
            for line in test_case_content.split('\n'):
                if line.strip() and not line.startswith('Test Case:'):
                    details += f"  {test_case} --> \"{line.strip()}\"\n"
        return details
