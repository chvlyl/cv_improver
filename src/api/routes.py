from fastapi import APIRouter, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import os

from src.services.resume_service import process_resume_and_job

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Paths to the example files
EXAMPLE_FILES_BASE_PATH = "example"
EXAMPLE_RESUME_PATH = os.path.join(EXAMPLE_FILES_BASE_PATH, "resume.md")
EXAMPLE_JOB_LINK_PATH = os.path.join(EXAMPLE_FILES_BASE_PATH, "job_link.md")
EXAMPLE_PERSONAL_WRITEUP_PATH = os.path.join(EXAMPLE_FILES_BASE_PATH, "personal_writeup.md")
EXAMPLE_OTHER_INFO_URL_PATH = os.path.join(EXAMPLE_FILES_BASE_PATH, "other_infor.md")

@router.get("/get_example_data", response_class=JSONResponse)
async def get_example_data():
    try:
        example_data = {}
        file_paths = {
            "resume_markdown": EXAMPLE_RESUME_PATH,
            "job_link": EXAMPLE_JOB_LINK_PATH,
            "personal_writeup": EXAMPLE_PERSONAL_WRITEUP_PATH,
            "other_information_url": EXAMPLE_OTHER_INFO_URL_PATH
        }
        
        for key, path in file_paths.items():
            if not os.path.exists(path):
                # Allow missing files, but return None or empty string for them
                example_data[key] = "" # Or None, depending on how frontend handles it
            else:
                with open(path, "r") as f:
                    example_data[key] = f.read().strip() # strip to remove leading/trailing whitespace
                    
        return example_data
    except Exception as e:
        # Log the exception for debugging
        print(f"Error reading example files: {e}")
        raise HTTPException(status_code=500, detail=f"Error reading example files: {str(e)}")

@router.post("/process_resume", response_class=HTMLResponse)
async def process_resume(request: Request, resume_markdown: str = Form(...), job_link: str = Form(...), other_information_url: str = Form(...), personal_writeup: str = Form(...)):
    try:
        # Process the resume using the service layer
        tailored_resume, interview_materials = process_resume_and_job(
            resume_markdown, job_link, other_information_url, personal_writeup
        )
        
        # Return the results
        return templates.TemplateResponse(
            "results.html", 
            {
                "request": request,
                "tailored_resume": tailored_resume,
                "interview_materials": interview_materials
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 