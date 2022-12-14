ADMIN_IDS = [123, ]
BASE_URL = "https://domain"
MAIN_BOT_TOKEN = "bot:token"
MAIN_BOT_PATH = "/webhook/main"

OTHER_BOTS_PATH = "/webhook/bot/{bot_token}"
OTHER_BOTS_URL = f"{BASE_URL}{OTHER_BOTS_PATH}"

WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_PORT = 8081

POSTGRES_HOST = "pgdb"
POSTGRES_PORT = 5432
POSTGRES_USER = 'cooluser'
POSTGRES_PASS = 'coolpass'
POSTGRES_DB = 'cooldb'
POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

REDIS_DSN = "redis://127.0.0.1:6479"


TEST_WEBHOOK = '2'