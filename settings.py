import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
API_ENDPOINT = os.environ.get("API_ENDPOINT")
API_KEY = os.environ.get("API_KEY")
DISCORD_ENDPOINT = os.environ.get("DISCORD_ENDPOINT")
