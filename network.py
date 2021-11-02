import requests
import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

from model import UserData, ApexUser
from settings import API_ENDPOINT, API_KEY, TINAX_API

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def fetchUserData(au: ApexUser) -> dict:
    res = requests.get(f"{API_ENDPOINT}/standard/profile/{au.platform}/{au.uid}?TRN-Api-Key={API_KEY}")

    if res.status_code != 200:
        return {"status": res.status_code, "user_data": None}

    response = res.json()

    timestamp = int(round(datetime.datetime.now().timestamp()))
    return {"status": res.status_code, "user_data": UserData(au, int(response["data"]["segments"][0]["stats"]["level"]["value"]), timestamp)}

def postRankUpdate(player_name: str, time: datetime.datetime, old_rank: int, new_rank: int) -> None:
    return requests.post(TINAX_API+"/rank/register", json={
        'player_name': player_name,
        'timestamp': int(time.timestamp()),
        'old_rank': old_rank,
        'new_rank': new_rank
    })

