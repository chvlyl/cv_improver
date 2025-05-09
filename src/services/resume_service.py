from src.cv_improver.crew import CvImprover
import tempfile
import os

def process_resume_and_job(resume_markdown: str, job_link: str, other_information_url: str, personal_writeup: str) -> tuple:
    """
    Process a user's resume for a specific job and return the tailored resume and interview materials
    
    Args:
        resume_markdown (str): The user's resume in markdown format
        job_link (str): URL of the job posting
        other_information_url (str): URL for other relevant information (e.g., GitHub, LinkedIn)
        personal_writeup (str): A brief write-up about the user
    
    Returns:
        tuple: (tailored_resume, interview_materials) both as markdown strings
    """
    # Create a temporary file for the resume
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_file:
        temp_file.write(resume_markdown)
        temp_resume_path = temp_file.name
    
    try:
        # Set up the job application inputs
        job_application_inputs = {
            'job_posting_url': job_link,
            'other_information_url': other_information_url,
            'personal_writeup': personal_writeup
        }
        
        # Process the resume using the CV Improver crew
        # Use the existing CvImprover class without modifying its logic
        crew_instance = CvImprover(temp_resume_path)
        crew = crew_instance.crew()
        crew_result = crew.kickoff(inputs=job_application_inputs)
        
        # Read the output files
        with open('tailored_resume.md', 'r') as f:
            tailored_resume = f.read()
        
        with open('interview_materials.md', 'r') as f:
            interview_materials = f.read()
        
        return tailored_resume, interview_materials
    
    finally:
        # Clean up the temporary resume file
        if os.path.exists(temp_resume_path):
            #os.remove(temp_resume_path) 
            pass