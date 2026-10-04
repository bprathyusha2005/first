import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""It adds your project’s root folder to Python’s import path, so you can import modules (like db, models, etc.)
 from outside the current script’s folder."""
from db import Base,engine
import models 

if __name__=="__main__":
    print("Creating tables")
    Base.metadata.create_all(bind=engine)
    print("Table creation successful:",list(Base.metadata.tables.keys()))