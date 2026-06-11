import os
import fastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
from itsdangerous import URLSafeSerializer

load_dotenv()

app = FastAPI()
