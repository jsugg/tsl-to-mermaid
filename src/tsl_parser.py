import re
from typing import List

class TSLParser:
    """
    Parses TSL (Test Script Language) scripts and extracts relevant information.
    """
    def __init__(self, tsl_script: str):
        self.tsl_script: str = tsl_script

    def extract_comments(self) -> List[str]:
        """
        Extracts comments from the TSL script.
        """
        return [line for line in self.tsl_script.split('\n') if line.startswith("#")]

    def extract_scenarios(self) -> List[str]:
        """
        Extracts test scenarios from the TSL script.
        """
        return re.findall(r"Test Scenario: (.+)", self.tsl_script)

    def extract_test_cases(self) -> List[str]:
        """
        Extracts test cases from the TSL script.
        """
        return re.findall(r"Test Case: (.+)", self.tsl_script)

    def is_valid(self) -> bool:
        """
        Validates the TSL script against required sections.
        """
        required_sections: List[str] = ["Test Scenario", "Test Case", "Description", "Preconditions", "Steps", "Expected Results"]
        for _ in self.extract_scenarios():
            for case in self.extract_test_cases():
                for section in required_sections:
                    if f"{section}: {case}" not in self.tsl_script:
                        return False
        return True
