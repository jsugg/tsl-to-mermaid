from .formats.mermaid_converter import MermaidConverter
from .formats.comments_converter import CommentsConverter
from .tsl_parser import TSLParser
from typing import Union

class ConverterFactory:
    """
    Factory to create different types of converters.
    """

    @staticmethod
    def create_converter(format_type: str, tsl_parser: TSLParser) -> Union[MermaidConverter, CommentsConverter]:
        """
        Creates a converter based on the specified format.
        """
        if format_type == "mermaid":
            return MermaidConverter(tsl_parser)
        elif format_type == "comments":
            return CommentsConverter(tsl_parser)
        else:
            raise ValueError("Invalid format type. Use 'mermaid' or 'comments'.")
