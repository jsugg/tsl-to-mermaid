import argparse
import sys
from src.tsl_parser import TSLParser
from src.converter_factory import ConverterFactory
from src.dependency_visualizer import DependencyVisualizer
from src.mermaid_renderer import MermaidRenderer

def main():
    parser = argparse.ArgumentParser(description="Convert TSL to Mermaid diagrams and validate.")
    parser.add_argument("input_file", help="Input TSL script file")
    parser.add_argument("output_file", help="Output Mermaid diagram or comments file")
    parser.add_argument("--format", choices=["mermaid", "comments"], default="mermaid", help="Output format")
    parser.add_argument("--visualize", action="store_true", help="Visualize test case dependencies")
    parser.add_argument("--svg", action="store_true", help="Convert to SVG format")
    parser.add_argument("--png", action="store_true", help="Convert to PNG format")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as file:
            tsl_script = file.read()
    except FileNotFoundError:
        print(f"Input file '{args.input_file}' not found.")
        sys.exit(1)

    tsl_parser = TSLParser(tsl_script)
    if not tsl_parser.is_valid():
        print("TSL script validation failed. Please check the script for errors.")
        sys.exit(1)

    converter = ConverterFactory.create_converter(args.format, tsl_parser)
    output = converter.convert()

    if args.visualize:
        visualizer = DependencyVisualizer(tsl_parser)
        dependencies_graph = visualizer.visualize()
        output += "\n\n/* Dependencies */\n" + dependencies_graph

    try:
        with open(args.output_file, "w") as file:
            file.write(output)
        print(f"Conversion completed. Output saved to '{args.output_file}'.")

        if args.svg:
            svg_success = MermaidRenderer.render_to_file(output, args.output_file.replace(".png", ".svg"), "svg")
            if svg_success:
                print(f"SVG conversion successful. Output saved to {args.output_file.replace('.png', '.svg')}")

        if args.png:
            png_success = MermaidRenderer.render_to_file(output, args.output_file.replace(".svg", ".png"), "png")
            if png_success:
                print(f"PNG conversion successful. Output saved to {args.output_file.replace('.svg', '.png')}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
