from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

from src.tensor-pilot-145.api.seo_data import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Tensor-Pilot-145 SEO API",
    description="Universal SEO skill for Claude Code - comprehensive data fetching and analysis",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the SEO API routes
app.include_router(router)

if __name__ == "__main__":
    logger.info("Starting Tensor-Pilot-145 SEO API...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
