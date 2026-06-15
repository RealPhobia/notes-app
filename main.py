import os
import fastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
from itsdangerous import URLSafeSerializer

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
serializer = URLSafeSerializer(SECRET_KEY)


def get_current_user(request: Request):
    cookies = request.cookies.get("session")
    if not cookie:
        return None
    try:
        data = serializer.load(cookie)
        return data
    except Exception:
        return None


@app.get("/")
def home(request: Request, user_id: str = Depends(get_current_user):
    return template.TemplateResponse("index.html", {"request": request, "user_id": user_id})

@app.get("/register")
def registration_page(request: Request):
    return template.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(email: str = Form(...), password: str = Form(...)):
    auth_res = supabase.auth.sign_up({"email": email, "password": password})
    if auth_res.user:
         return ResponseRedirect("/login", status_code=302)
    return {"error": "Registration Failed"}

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def 
