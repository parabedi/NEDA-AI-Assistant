from fastapi import FastAPI

from app.api.tasks import router as task_router

app = FastAPI(title="NEDA AI Assistant")


@app.get("/")
def root():
    return {"message": "Welcome to NEDA"}


app.include_router(task_router)