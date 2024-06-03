import os
from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")
IS_DEVELOPMENT = ENVIRONMENT == "local"
IS_LOCAL = ENVIRONMENT == "local"
IS_STAGING = ENVIRONMENT == "staging"
DB_URL = os.getenv("DB_URL")
DB_NAME = os.getenv("DB_NAME")
PROXY_CSV_URL = os.getenv("PROXY_CSV_URL")
SLACK_HEADER = os.getenv("SLACK_HEADER")
API_KEY_SCRAPY = os.getenv("API_KEY_SCRAPY")
ELASTIC_SEARCH_URL = os.getenv("ELASTIC_SEARCH_URL")
ELASTIC_SEARCH_USERNAME = os.getenv("ELASTIC_SEARCH_USERNAME")
ELASTIC_SEARCH_PASSWORD = os.getenv("ELASTIC_SEARCH_PASSWORD")
REDIS_PORT = 6380
REDIS_DB = 0

REDIS_URL = os.getenv("REDIS_URL")
