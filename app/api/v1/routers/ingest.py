import magic
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, status, Request, Depends
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import Annotated
from pinecone.db_data.index_asyncio_interface import IndexAsyncioInterface
from app.util import is_pdf_empty_or_image_only, extract_file_by_type
from app.util.hash_value import HashManager
from app.services import embedding_service
from app.api.deps import get_pinecone_index
from app.api.deps import get_current_key
from app.db.models import AccessKeys

ingest_router = APIRouter()

ALLOWED_EXTENSIONS = [
    'csv','pdf','txt'
]

ALLOWED_MIME_TYPES = [
    'text/csv',
    'application/pdf',
    'text/plain'
]

MAGIC_MIME_TYPES = {
    "text/csv": "csv",
    "application/pdf": "pdf",
    "text/plain": "txt"
}

MAX_FILE_SIZE = 8 * 1024 * 1024

CHUNK_SIZE = 50
CHUNK_OVERLAP = 30

@ingest_router.post('/upload')
async def upload_file_and_embed(
    request: Request,
    pinecone_index: Annotated[IndexAsyncioInterface, Depends(get_pinecone_index)],
    key: Annotated[AccessKeys, Depends(get_current_key)],
    file: UploadFile = File(...)
):
    
    # Bytes and file metadata initialization
    header_bytes = await file.read(2048) # Reads first 2048 bytes
    sanitized_mime_type = magic.from_buffer(header_bytes, mime=True)
    
    file_size = file.size

    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            details="File is required!"
        )

    if sanitized_mime_type not in MAGIC_MIME_TYPES:
        raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid file format. Only CSV, PDF, and TXT Files are accepted"
                )

    # Maximum file size guard 8MB MAX
    if (file_size) and file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum file size is 8MB"
        )


    remaining_bytes = await file.read()
    full_file_bytes = header_bytes + remaining_bytes

    # Checks if the user only uploads pdf file that looks like scanned and only images
    if MAGIC_MIME_TYPES[sanitized_mime_type] == "pdf" and is_pdf_empty_or_image_only(full_file_bytes):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="PDF File only contains Image or non text content."
        )

    # Returns array of documents contents with metadata or if txt the whole content
    contents = extract_file_by_type(MAGIC_MIME_TYPES[sanitized_mime_type], full_file_bytes)

    final_chunks = []

    # Splitting or Chunking where if csv it will be return because it's already splitted properly using /n else it should be splitted
    if MAGIC_MIME_TYPES[sanitized_mime_type] == 'csv':
        final_chunks = contents['content']
    else:
        splitter = RecursiveCharacterTextSplitter(
            separators=["\n"," ", ""],
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        final_chunks = splitter.split_documents(contents['content'])

    # Embedding by chunked texts in order to store some of the metadata
    doc_id = str(uuid.uuid4())
    records = []
    chunk_texts = [chunk.page_content for chunk in final_chunks]
    vectors = embedding_service(chunk_texts)

    for chunk_index, (chunk, vector) in enumerate(zip(final_chunks, vectors)):
        text = chunk.page_content

        records.append({
            "id": doc_id,
            "values": vector,
            "metadata": {
                "text": text
            }
        })

    result = await pinecone_index.upsert(
        vectors=records,
        namespace=str(key.id)
    )

    print(f'Namespace: {str(key.id)}')
    print(f'Pinecone result: {result}')

    

    return { "message": "File processed successfully!" }

    



    

    
    

    
    
    


    


