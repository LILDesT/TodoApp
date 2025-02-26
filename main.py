from fastapi import FastAPI, Request, HTTPException

import logging

from database import engine

import models
from routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # Change to DEBUG to capture more detailed logs


@app.get("/") 
def test(request: Request):
    logging.info("Root endpoint accessed")  # Log when the root endpoint is accessed
    return templates.TemplateResponse("home.html", {"request": request})

# Add exception handling middleware
@app.middleware("http")
async def add_exception_logging(request: Request, call_next):
    logging.info(f"Request path: {request.url.path}")  # Log the request path
    try:
        response = await call_next(request)
        return response

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")  # Raise HTTPException for better error handling



app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
