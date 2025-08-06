# Docling OCR Project

This project demonstrates two key OCR functionalities using the Docling library:

1. **Force Full Page OCR** - Performs OCR on entire PDF pages with table structure detection
2. **Automatic OCR Language Detection** - Uses Tesseract's automatic language detection feature

## Setup Instructions

### 1. Install Python Dependencies

```bash
python -m venv docling_env
.\docling_env\Scripts\activate
pip install -r requirements.txt
```

### 2. Install Tesseract OCR

#### Windows:
1. Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install it and add to PATH
3. Or use chocolatey: `choco install tesseract`

#### macOS:
```bash
brew install tesseract
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt-get install tesseract-ocr
```

### 3. Prepare Your PDF File

Place your PDF file in the `data/` folder and name it `sample.pdf`, or modify the `input_doc_path` variable in `main.py` to point to your PDF file.

## Usage

Run the main script:

```bash
python main.py
```

The script will:
1. Create a `data/` folder if it doesn't exist
2. Check for your PDF file
3. Run both OCR examples
4. Save the results as markdown files in the `data/` folder

## Output Files

- `data/full_page_ocr_output.md` - Results from force full page OCR
- `data/auto_lang_detection_output.md` - Results from automatic language detection

## Features Demonstrated

### Example 1: Force Full Page OCR
- Enables OCR on entire PDF pages
- Includes table structure detection
- Uses Tesseract CLI OCR engine
- Saves output as markdown

### Example 2: Automatic Language Detection
- Uses Tesseract's automatic language detection
- Forces full page OCR
- Automatically detects the language of text in the PDF

## Troubleshooting

1. **Tesseract not found**: Make sure Tesseract is installed and in your PATH
2. **PDF file not found**: Place your PDF in the `data/` folder or update the path in `main.py`
3. **Import errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`

## References

- [Docling Full Page OCR Example](https://docling-project.github.io/docling/examples/full_page_ocr/)
- [Docling Automatic Language Detection Example](https://docling-project.github.io/docling/examples/tesseract_lang_detection/) 