from pathlib import Path
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import VlmPipelineOptions, HuggingFaceVlmOptions, InferenceFramework, ResponseFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.pipeline.vlm_pipeline import VlmPipeline


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

    print("=== VLM Pipeline with SmolDocling (Corrected Image Processing) ===")
    print("Using SmolDocling-256M-preview model for document understanding...")
    
    try:
        # Create SmolDocling VLM options with correct image processing
        # Based on model config: image_size=512, max_image_size=512
        smoldocling_options = HuggingFaceVlmOptions(
            repo_id='ds4sd/SmolDocling-256M-preview',  # SmolDocling model (verified online)
            prompt='Convert this page to docling.',     # SmolDocling prompt
            load_in_8bit=True,                         # Use 8-bit quantization for efficiency
            llm_int8_threshold=6.0,                    # Int8 threshold for quantization
            quantized=False,                           # Don't use quantized model
            inference_framework=InferenceFramework.TRANSFORMERS,  # Use transformers framework
            response_format=ResponseFormat.DOCTAGS,    # Use doctags format for better structure
        )
        
        # Create VLM pipeline options with correct image processing
        # SmolDocling expects 512px longest edge, so we scale accordingly
        pipeline_options = VlmPipelineOptions(
            vlm_options=smoldocling_options,
            images_scale=0.25,                         # Scale to ~512px longest edge (2048 * 0.25 = 512)
            generate_page_images=True,                 # Generate page images
            generate_picture_images=False,             # Don't generate picture images
        )
        
        # Create converter with SmolDocling VLM pipeline
        converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_cls=VlmPipeline,
                    pipeline_options=pipeline_options,
                ),
            }
        )
        
        print("SmolDocling VLM pipeline initialized successfully!")
        print("Converting document with SmolDocling Vision Language Model...")
        print("Note: Images scaled to 25% (512px longest edge) to match model requirements.")
        
        # Convert the document using SmolDocling VLM pipeline
        doc = converter.convert(input_doc_path).document
        
        # Export to markdown
        md = doc.export_to_markdown()
        
        print("SmolDocling VLM conversion completed successfully!")
        print("First 500 characters of markdown output:")
        print(md[:500] + "..." if len(md) > 500 else md)
        
        # Save the markdown output
        output_file = data_folder / "smoldocling_output.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Full SmolDocling output saved to: {output_file}")
        
        # Show some statistics about the document
        print(f"\nDocument Statistics:")
        print(f"Total pages: {len(doc.pages)}")
        print(f"Total blocks: {sum(len(page.blocks) for page in doc.pages)}")
        
        # Count different types of content
        tables = sum(len(page.tables) for page in doc.pages)
        figures = sum(len(page.figures) for page in doc.pages)
        print(f"Tables detected: {tables}")
        print(f"Figures detected: {figures}")
        
        print(f"\nSmolDocling Model Info:")
        print(f"Model: ds4sd/SmolDocling-256M-preview (verified online)")
        print(f"Model Config: image_size=512, max_image_size=512")
        print(f"Quantization: 8-bit (efficient)")
        print(f"Framework: Transformers")
        print(f"Response Format: Doctags (structured output)")
        print(f"Image Scale: 25% (matches model's 512px requirement)")
        
    except Exception as e:
        print(f"Error in SmolDocling VLM pipeline conversion: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you have enough RAM (8GB+ recommended)")
        print("2. Ensure stable internet connection for model download")
        print("3. Try with a smaller PDF file first")
        print("4. The image scaling is set to 25% to match SmolDocling's 512px requirement")
        print("5. If still failing, try with a PDF that has smaller images")
        
        # Fallback to regular conversion if VLM fails
        print("\nFalling back to regular conversion...")
        try:
            from docling.document_converter import DocumentConverter as RegularConverter
            regular_converter = RegularConverter()
            doc_fallback = regular_converter.convert(input_doc_path).document
            md_fallback = doc_fallback.export_to_markdown()
            
            output_file_fallback = data_folder / "fallback_output.md"
            with open(output_file_fallback, 'w', encoding='utf-8') as f:
                f.write(md_fallback)
            print(f"Fallback output saved to: {output_file_fallback}")
            
        except Exception as fallback_error:
            print(f"Fallback conversion also failed: {fallback_error}")


if __name__ == "__main__":
    main() 