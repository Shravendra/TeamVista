from fastapi import FastAPI
from src.utils.database import engine, Base
from src.routes import auth, user_routes, team_routes, city_routes

# Initialize FastAPI app
app = FastAPI(
    title="Smart Dashboard",
    description="API for managing employee status and process tracking",
    version="1.0.0",
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(team_routes.router, prefix="/teams", tags=["Teams"])
app.include_router(city_routes.router, prefix="/cities", tags=["Cities"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Smart Dashboard API"}
