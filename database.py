from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
load_dotenv()
connection_string = os.getenv("CONNECTION_STRING")

engine = create_engine(connection_string)

def get_student_records():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM Student"))
        records = result.fetchall()
        return records

