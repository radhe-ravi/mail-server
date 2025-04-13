import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GMAIL_USER = os.getenv("GMAIL_USER")
    GMAIL_PASS = os.getenv("GMAIL_PASS")
