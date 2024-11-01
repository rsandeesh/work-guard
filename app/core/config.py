# ====== Common Configurations ======
import os

API_PREFIX = "/api/v1"

# ======= Authentication Configs =============
SECRET_KEY = os.getenv("SECRET_KEY", "2c83aaba1de8a08503630fa6c5809d88cfbab7b47fe5a3ba554e5e0e6843f178")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRATION_MINUTES = 30

# ====== PostgreSQL database ======
DBUSER = os.getenv("DBUSER", "postgres")
DBPASS = os.getenv("DBPASS", "mysecretpassword")
DBHOST_FULL = os.getenv(
    "DBHOST_FULL", "localhost:5432"
)
DATABASE = os.getenv(
    "DATABASE", "postgres"
)
POSTGRES_CONNECTION_STRING = (
    f"postgresql+psycopg://{DBUSER}:{DBPASS}@{DBHOST_FULL}/{DATABASE}"
)