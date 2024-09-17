import redis.asyncio as redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as translation_router
from app.core.config import settings
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

app = FastAPI(
    title="NTQ AI - Machine Translation API",
    description="API for translating text and detecting languages",
    version="1.0.0",
)


# @app.on_event("startup")
# async def startup():
#     """Initialize Redis connection and FastAPI limiter during app startup."""
#     redis_url = (
#         f"redis://{settings.REDIS_USER}:{settings.REDIS_PASSWORD}"
#         f"@{settings.REDIS_HOST}:{settings.REDIS_PORT}/0"
#     )
#     redis_connection = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)
#     await FastAPILimiter.init(redis_connection)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the translation API router
app.include_router(translation_router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint to welcome users to the API."""
    return {"message": "Welcome to the Machine Translation API"}


@app.get("/health")
async def health_check():
    """Health check endpoint to verify that the API is running."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    # Run the application using uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=4000, reload=True)