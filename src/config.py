from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_TYPE = "sqlite"

DATABASE_PATH = BASE_DIR / "data" / "maritime.db"

LOG_FOLDER = BASE_DIR / "logs"

LOG_FILE = LOG_FOLDER / "maritime.log"

# Later

# DATABASE_TYPE = "postgresql"
# HOST = "localhost"
# PORT = 5432
# DATABASE = "maritime"
# USER = "postgres"
# PASSWORD = "xxxxx"

