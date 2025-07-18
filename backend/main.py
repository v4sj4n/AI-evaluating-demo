from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from jobs.routes import jobs_router
from applicants.routes import applicants_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(jobs_router)
app.include_router(applicants_router)