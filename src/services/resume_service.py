from src.cv_improver.crew import CvImprover
import tempfile
import os

def process_resume_and_job(resume_markdown: str, job_link: str) -> tuple:
    """
    Process a user's resume for a specific job and return the tailored resume and interview materials
    
    Args:
        resume_markdown (str): The user's resume in markdown format
        job_link (str): URL of the job posting
    
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
            'github_url': 'https://github.com/joaomdmoura',
            'personal_writeup': """Noah is an accomplished Software
            Engineering Leader with 18 years of experience, specializing in
            managing remote and in-office teams, and expert in multiple
            programming languages and frameworks. He holds an MBA and a strong
            background in AI and data science. Noah has successfully led
            major tech initiatives and startups, proving his ability to drive
            innovation and growth in the tech industry. Ideal for leadership
            roles that require a strategic and innovative approach."""
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