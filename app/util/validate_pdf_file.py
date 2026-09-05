from pypdf import PdfReader
from io import BytesIO
from fastapi import HTTPException, status

def is_pdf_empty_or_image_only(file_bytes: bytes) -> bool:
    """ Extracts text from PDF. Returns True if pdf is empty of if the user only upload scanned whole image in pdf format"""
    try:
        reader = PdfReader(BytesIO(file_bytes))
        total_text = ""

        for page in reader.pages[:5]:
            text = page.extract_text()
            if text:
                total_text += text.strip()
        return len(total_text) < 10 

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The PDF file is corrupted or unreadable."
        )