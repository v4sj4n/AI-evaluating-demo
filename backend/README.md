# AI Evaluating Demo - Backend

## Description
A Python backend application for AI evaluation demonstrations, showcasing model assessment and comparison capabilities.

## Installation
```bash
# Clone the repository
git clone <repository-url>
cd backend

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

## Usage
```bash
# Start the development server
uv run python app.py
```

## Development
```bash
# Add new dependencies
uv add <package-name>

# Run in development mode
uv run fastapi dev
```

## API Endpoints

### Jobs
- `GET /jobs/` - Get Jobs
- `POST /jobs/` - Create Job
- `GET /jobs/{job_id}` - Get Job
- `PUT /jobs/{job_id}` - Update Job
- `DELETE /jobs/{job_id}` - Delete Job

### Applicants
- `GET /applicants/` - Get Applicants
- `POST /applicants/` - Create Applicant
- `GET /applicants/{applicant_id}` - Get Applicant
- `PUT /applicants/{applicant_id}` - Update Applicant
- `DELETE /applicants/{applicant_id}` - Delete Applicant

## Technologies Used
- Python
- uv (Python package manager)
- FastAPI
- sqlalchemy + psycopg2

## Contributing
Instructions for contributing to the project.

## License
Your license information.