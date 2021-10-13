import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def fetchUserData(platform: str, uid: str):
    API_KEY = os.environ.get("API_KEY")
    res = requests.get(f"https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{uid}?TRN-Api-Key={API_KEY}")

    response = res.json()


