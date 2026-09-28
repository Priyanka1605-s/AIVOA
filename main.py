from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.deviations import router as deviations_router

app = FastAPI(
    title="AIVOA Deviation Intake API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    deviations_router
)


@app.get("/")
def root():
    return {
        "message": "AIVOA Deviation Intake API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }