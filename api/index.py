from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from .github_trending import get_trending_repositories

app = FastAPI(title="GitHub Trending API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Response Models
class Repository(BaseModel):
    repo_name: str
    link: str
    language: str
    stars: int
    forks: int
    description: str
    stars_in_period: int

class TrendingResponse(BaseModel):
    status: str
    data: List[Repository]

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Welcome to GitHub Trending API"})

@app.get("/api/trending", response_model=TrendingResponse)
async def get_trending(time_frame: str = "daily"):
    """
    Get trending repositories from GitHub
    """
    try:
        repositories = get_trending_repositories(time_frame)
        return JSONResponse(
            content={
                "status": "success",
                "data": repositories
            }
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 