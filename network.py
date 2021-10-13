import requests
import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

from model import UserData, ApexUser

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def fetchUserData(au: ApexUser) -> dict:
    API_KEY = os.environ.get("API_KEY")
    res = requests.get(f"https://public-api.tracker.gg/v2/apex/standard/profile/{au.platform}/{au.uid}?TRN-Api-Key={API_KEY}")

    if res.status_code != 200:
        return {"status": res.status_code, "user_data": None}

    response = res.json()

    timestamp = int(round(datetime.datetime.now().timestamp()))
    return {"status": res.status_code, "user_data": UserData(au, int(response["data"]["segments"][0]["stats"]["level"]["value"]), timestamp)}


