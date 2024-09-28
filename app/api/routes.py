from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from uuid import UUID
from app.models.user import User

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
  return await UserService.create_user(user)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: UUID):
  user = await UserService.get_user(user_id)
  if user is None:
    raise HTTPException(status_code=404, detail="User not found") 
  return user

@router.get("/users", response_model=list[UserResponse])
async def get_users():
  return await UserService.get_users()