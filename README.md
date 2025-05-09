# CvImprover - Resume Tailoring Web Application

Welcome to the CvImprover project, a web application powered by [crewAI](https://crewai.com). This application helps users tailor their resumes for specific job postings and provides interview preparation materials.

## Features

- **Resume Tailoring**: Upload your resume in markdown format and provide a job posting URL to get a tailored resume that highlights your most relevant experience and skills.
- **Interview Preparation**: Receive interview materials with potential questions and talking points specific to the job.
- **Web Interface**: User-friendly web interface with markdown rendering, copy to clipboard, and download functionality.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

```
pip install crewai
pip install 'crewai[tools]'
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Configuration

**Add your `OPENAI_API_KEY` into the `.env` file**

## Running the Web Application

To start the web application, run this from the root folder of your project:

```
source .venv/bin/activate
```

```bash
python main.py
```

This will start the FastAPI web server on http://0.0.0.0:8000. You can then access the application through your web browser.

## Running the CLI Version

To run the CLI version of the resume tailoring tool, use:

```bash
$ crewai run
```

## Project Structure

- `main.py`: FastAPI main entry point
- `src/cv_improver/`: Core business logic for resume tailoring
- `src/api/`: API endpoints
- `src/services/`: Service layer
- `static/`: Static assets (CSS, JavaScript)
- `templates/`: HTML templates for the web interface
- `tests/`: Test files

## Customizing

- Modify `src/cv_improver/config/agents.yaml` to define your agents
- Modify `src/cv_improver/config/tasks.yaml` to define your tasks
- Modify `src/cv_improver/crew.py` to add your own logic, tools and specific args

## Support

For support, questions, or feedback regarding the CvImprover or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
