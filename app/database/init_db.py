from app.database.database import Base, engine

# Import all models
from app.models.task import Task

def init_db():
  Base.metadata.create_all(bind=engine)
  print("Database and tables created successfully.")

if __name__=="__main__" :
   init_db()