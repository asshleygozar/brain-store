import pypdf
import io
import csv
from langchain_core.documents import Document
from fastapi import  HTTPException, status

def extract_file_by_type(file_type: str, bytes: bytes):
    match file_type:
        case 'csv':
            return extract_csv_content(bytes)
        case 'pdf':
            return extract_pdf_content(bytes)
        case 'txt':
            return extract_txt_content(bytes)
        case _:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"File type: {file_type} is not accepted")

# For .pdf files content extraction
def extract_pdf_content(bytes: bytes):
    """Extracts content from pdf file page by page"""
    # Wraps into file like object so pypdf can read it
    pdf_stream = io.BytesIO(bytes)

    try:
        # Holds into RAM so it can be processed
        pdf_reader = pypdf.PdfReader(pdf_stream)

        documents = []

        # Reads each page and extracts its content then gets stored as Document in documents array
        for page_num, page in enumerate(pdf_reader.pages):
            text = page.extract_text()

            if text:
                doc = Document(
                    page_content=text,
                    metadata={"page": page_num}
                )
                documents.append(doc)

        return {
            "content": documents
        }
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Pdf file content cannot be extracted")

# For .csv files content extraction
def extract_csv_content(bytes: bytes):
    """Extracts csv content from csv byte row by row"""

    text_content = bytes.decode('utf-8')
    csv_stream = io.StringIO(text_content)
     
    try:
        csv_reader = csv.DictReader(csv_stream)
        documents = []

        for row_index, row in enumerate(csv_reader):
            # Format the dictionary into readable string
            # Example: "Name": Asshley\nAge:21 Uses the separator next line so it would be easier to identify later on using CharacterTextSplitter
            row_text = "\n".join([f"{key.strip()}: {value.strip()}" for key, value in row.items() if value])

            doc = Document(page_content=row_text, metadata={"row_index": row_index})
            documents.append(doc)

        return {"content": documents}


    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error parsing csv")

# For .txt files extraction
def extract_txt_content(bytes: bytes):
    """Extracts content from txt file as a whole"""
    try:
        text_content = bytes.decode('utf-8')

        document = Document(
            page_content=text_content,
        )

        return {
            "content": [document]
        }

    except UnicodeDecodeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='File could not be decode into utf-8.')


