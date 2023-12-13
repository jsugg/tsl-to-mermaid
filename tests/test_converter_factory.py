import pytest
from src.tsl_parser import TSLParser
from src.converter_factory import ConverterFactory
from src.formats.mermaid_converter import MermaidConverter
from src.formats.comments_converter import CommentsConverter

def test_create_mermaid_converter():
    parser = TSLParser("Test Case: TC1")
    converter = ConverterFactory.create_converter("mermaid", parser)
    assert isinstance(converter, MermaidConverter)

def test_create_comments_converter():
    parser = TSLParser("# Comment")
    converter = ConverterFactory.create_converter("comments", parser)
    assert isinstance(converter, CommentsConverter)

def test_invalid_converter_type():
    parser = TSLParser("Test Case: TC1")
    with pytest.raises(ValueError):
        ConverterFactory.create_converter("invalid", parser)
