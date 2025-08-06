#!/usr/bin/env python3
"""
Test script to verify Docling setup and imports
"""

def test_imports():
    """Test that all required imports work correctly"""
    try:
        from pathlib import Path
        print("✓ pathlib imported successfully")
        
        from docling.datamodel.base_models import InputFormat
        print("✓ InputFormat imported successfully")
        
        from docling.datamodel.pipeline_options import (
            PdfPipelineOptions,
            TesseractCliOcrOptions,
        )
        print("✓ Pipeline options imported successfully")
        
        from docling.document_converter import DocumentConverter, PdfFormatOption
        print("✓ Document converter imported successfully")
        
        print("\n🎉 All imports successful! Your Docling environment is ready.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def test_tesseract_availability():
    """Test if Tesseract is available on the system"""
    import subprocess
    import shutil
    
    try:
        # Check if tesseract is in PATH
        tesseract_path = shutil.which('tesseract')
        if tesseract_path:
            print(f"✓ Tesseract found at: {tesseract_path}")
            
            # Try to get version
            result = subprocess.run(['tesseract', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                print(f"✓ Tesseract version: {version_line}")
                return True
            else:
                print("⚠ Tesseract found but version check failed")
                return False
        else:
            print("❌ Tesseract not found in PATH")
            print("Please install Tesseract OCR:")
            print("  Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
            print("  macOS: brew install tesseract")
            print("  Linux: sudo apt-get install tesseract-ocr")
            return False
            
    except subprocess.TimeoutExpired:
        print("⚠ Tesseract version check timed out")
        return False
    except Exception as e:
        print(f"❌ Error checking Tesseract: {e}")
        return False


def main():
    print("🔍 Testing Docling Setup...\n")
    
    # Test imports
    imports_ok = test_imports()
    
    print("\n" + "="*50 + "\n")
    
    # Test Tesseract
    tesseract_ok = test_tesseract_availability()
    
    print("\n" + "="*50 + "\n")
    
    if imports_ok and tesseract_ok:
        print("✅ Setup complete! You can now run main.py with a PDF file.")
        print("\nNext steps:")
        print("1. Place a PDF file in the data/ folder (name it 'sample.pdf')")
        print("2. Run: python main.py")
    elif imports_ok:
        print("⚠ Docling is installed but Tesseract is missing.")
        print("Please install Tesseract OCR to use the OCR features.")
    else:
        print("❌ Setup incomplete. Please check the error messages above.")


if __name__ == "__main__":
    main() 