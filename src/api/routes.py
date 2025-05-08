from fastapi import APIRouter, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.services.resume_service import process_resume_and_job

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/process_resume", response_class=HTMLResponse)
async def process_resume(request: Request, resume_markdown: str = Form(...), job_link: str = Form(...)):
    try:
        # Process the resume using the service layer
        tailored_resume, interview_materials = process_resume_and_job(
            resume_markdown, job_link
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