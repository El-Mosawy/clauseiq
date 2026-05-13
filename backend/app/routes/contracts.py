from fastapi import APIRouter # API router handles routing for contract-related endpoints
from fastapi import HTTPException # for raising HTTP exceptions with specific status codes and messages
from fastapi import UploadFile, File # for handling file uploads in the API

router = APIRouter() # create an instance

@router.post("/upload") # define a POST endpoint for uploading contracts
async def upload_contract(file: UploadFile = File(...)): # async because it may involve file handling or database operations ... means have to provide a file when calling this endpoint
    
    # check file type
    # Use content_type to determine whether we have a PDF or DOCX file. This is important for security to prevent malicious files from harming the app
    # If neither, raise error
    if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are accepted")
    
    # Check file size (can change based on needs for now its ok)
    if file.size > 25 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size must be under 25MB")
    
    return {
        "filename": file.filename,
        "content_type": file.content_type, # type of file (pdf etc.)
        "size_bytes": file.size, # size of file in bytes
        "message": "File received successfully"
    }