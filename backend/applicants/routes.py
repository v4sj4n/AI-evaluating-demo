from fastapi import APIRouter

applicants_router = APIRouter(prefix="/applicants", tags=["applicants"])

@applicants_router.get("/")
async def get_applicants():
    return {"message": "List of applicants"}   

@applicants_router.get("/{applicant_id}")
async def get_applicant(applicant_id: int):
    return {"message": f"Details of applicant {applicant_id}"}


@applicants_router.post("/")
async def create_applicant(applicant: dict):
    return {"message": "Applicant created", "applicant": applicant}

@applicants_router.put("/{applicant_id}")
async def update_applicant(applicant_id: int, applicant: dict):
    return {"message": f"Applicant {applicant_id} updated", "applicant": applicant}

@applicants_router.delete("/{applicant_id}")
async def delete_applicant(applicant_id: int):
    return {"message": f"Applicant {applicant_id} deleted"}