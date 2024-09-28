from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.routes import router as api_router
app = FastAPI()

@app.on_event("startup")
async def startup_event():
  init_db()

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root(): 
  return {"message": "Hello World"}