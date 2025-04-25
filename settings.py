import os

from starlette.config import Config
from starlette.staticfiles import StaticFiles

static_files = StaticFiles(
    directory="./static"
)

config = Config(".env")
JWT_SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY")
JWT_ALGO: str = os.environ.get("ALGORITHM")
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")
