from app.schemas.user import UserCreate
from app.models.user import User
from uuid import UUID

class UserService: 
  @staticmethod
  async def create_user(user: UserCreate):
    return User.create(name=user.name, email=user.email)

  @staticmethod
  async def get_user(user_id: UUID):
    return User.get(id=user_id)

  @staticmethod
  async def get_users():
    return User.objects.all()