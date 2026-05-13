# API = contract between any 2 systems that sets rules on how they can communicate with each other.
# FastAPI = a web framework that helps us build APIs quickly and efficiently by providing tools and features for handling requests, responses, and data validation. 
# These tools consist of automatic documentation, data validation, and dependency injection. It allows us to define our API endpoints using Python type hints, which helps with code readability and provides automatic validation of incoming data. FastAPI also generates interactive API documentation using Swagger UI and ReDoc, making it easier for developers to understand and test the API. Overall, FastAPI is a powerful framework that simplifies the process of building APIs while ensuring high performance and reliability.

from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware # just allows frontend and backend to talk without issues eventhough they are on different ports. Helps prevent harmful requests from other origins.
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

app = FastAPI( # Creates instance of FastAPI application which will be used to define API endpoints and handle incoming requests.
    title="ClauseIQ API",
    description="AI-powered contract intelligence for freelancers and agencies",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Allow requests from this origin (frontend running on this port)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# simple endpoint to check if API is running
@app.get("/health") # decorator that defines a get endpoint
def health_check():
    return {"status": "ok", "service": "clauseiq-api"}