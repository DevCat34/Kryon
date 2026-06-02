# ---------------- CONFIG ----------------

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")  # Guardar token en .env

DATA_FILE = "data.json"

MAX_TIMEOUT_SECONDS = 28 * 24 * 3600  # 28 días