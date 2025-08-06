from pathlib import Path
from docling.document_converter import DocumentConverter


def main():
    # Create a data folder for test documents
    data_folder = Path(__file__).parent / "data"
    data_folder.mkdir(exist_ok=True)
    
    # You can replace this with your own PDF file path
    # For now, we'll use a placeholder path
    input_doc_path = data_folder / "sample.pdf"
    
    # Check if the file exists, if not, create a placeholder
    if not input_doc_path.exists():
        print(f"Please place your PDF file at: {input_doc_path}")
        print("Or modify the input_doc_path variable to point to your PDF file.")
        return

    print("=== Minimal Docling Example ===")
    print("Converting PDF to markdown using default settings...")
    
    # Create converter with default settings (minimal configuration)
    converter = DocumentConverter()
    
    try:
        # Convert the document
        doc = converter.convert(input_doc_path).document
        
        # Export to markdown
        md = doc.export_to_markdown()
        
        print("Conversion completed successfully!")
        print("First 500 characters of markdown output:")
        print(md[:500] + "..." if len(md) > 500 else md)
        
        # Save the markdown output
        output_file = data_folder / "minimal_output.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Full output saved to: {output_file}")
        
    except Exception as e:
        print(f"Error in conversion: {e}")


if __name__ == "__main__":
    main() 