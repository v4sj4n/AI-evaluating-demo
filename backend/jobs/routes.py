from fastapi import APIRouter


jobs_router = APIRouter(prefix="/jobs", tags=["jobs"])

@jobs_router.get("/")
async def get_jobs():
    return {"message": "List of jobs"}

@jobs_router.get("/{job_id}")
async def get_job(job_id: int):
    return {"message": f"Details of job {job_id}"}

@jobs_router.post("/")
async def create_job(job: dict):
    return {"message": "Job created", "job": job}

@jobs_router.put("/{job_id}")
async def update_job(job_id: int, job: dict):
    return {"message": f"Job {job_id} updated", "job": job}

@jobs_router.delete("/{job_id}")
async def delete_job(job_id: int):
    return {"message": f"Job {job_id} deleted"}