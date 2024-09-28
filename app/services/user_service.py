from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User
from uuid import UUID

class UserService: 
  @staticmethod
  async def create_user(user: UserCreate):
    return User.create(name=user.name, email=user.email)

  @staticmethod
  async def get_user(user_id: UUID):
    try: 
      user = User.get(id=user_id)
    except User.DoesNotExist:
      return None
    return user

  @staticmethod
  async def get_users():
    return User.objects.all()

  @staticmethod
  async def update_user(user_id:UUID, user: UserUpdate):
    user = User.get(id=user_id)
    user.update(name=user.name, email=user.email)
    return user

  @staticmethod
  async def delete_user(user_id: UUID):
    user = User.get(id=user_id)
    user.delete()
    return user