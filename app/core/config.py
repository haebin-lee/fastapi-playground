try: 
  from pydantic_settings import BaseSettings
except ImportError: 
  from pydantic import BaseSettings
  
class Settings(BaseSettings): 
  PROJECT_NAME: str = "FastAPI SyllaDB Project"
  SYLLADB_KEYSPACE: str = "mykeyspace"
  SYLLADB_HOSTS: list = ["127.0.0.1"]

  class Config: 
    env_file = ".env"

settings = Settings()