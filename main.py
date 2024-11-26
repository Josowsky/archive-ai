from pdf2image import convert_from_path
from pytesseract import image_to_string

def extract_text_from_pdf(pdf_path):
    try:
        pages = convert_from_path(pdf_path, 300)
        text = ""

        for i, page in enumerate(pages):
            print(f"Processing page {i + 1} with OCR...")
            text += image_to_string(page, lang="eng") + "\n--- End of Page ---\n"

        return text

    except Exception as e:
        print(f"Error performing OCR: {e}")
        return None

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    extracted_text = extract_text_from_pdf(pdf_path)

    if extracted_text:
        print("\nExtracted Text:")
        print(extracted_text)
