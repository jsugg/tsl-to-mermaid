from .base_converter import BaseConverter
from ..tsl_parser import TSLParser

class CommentsConverter(BaseConverter):
    """
    Converts TSL script content to extract only the comments.
    """

    def __init__(self, tsl_parser: TSLParser):
        self.tsl_parser: TSLParser = tsl_parser

    def convert(self) -> str:
        """
        Extracts comments from the TSL script.
        """
        return "\n".join(self.tsl_parser.extract_comments())
