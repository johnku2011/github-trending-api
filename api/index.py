from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/")
async def read_root():
    return {"message": "Welcome to GitHub Trending API"}

@app.get("/api/trending")
async def get_trending(time_frame: str = "daily"):
    """
    Get trending repositories from GitHub
    """
    try:
        repositories = get_trending_repositories(time_frame)
        return {"status": "success", "data": repositories}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 