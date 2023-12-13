import subprocess

class MermaidRenderer:
    """
    Singleton class for rendering Mermaid diagrams to file.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MermaidRenderer, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def render_to_file(mermaid_code: str, output_file: str, format_type: str) -> bool:
        """
        Renders the given Mermaid code to a file in the specified format.
        """
        try:
            subprocess.run(["mmdc", "-i", "mermaid", "-o", output_file, "-b", "transparent" if format_type == "png" else None], input=mermaid_code, text=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error while converting to {format_type.upper()}: {e}")
            return False
