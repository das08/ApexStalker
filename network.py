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
    uid = response["data"]["platformInfo"]["platformUserId"]

    if uid != au.uid:
        return {"status": 404, "user_data": None}

    level = int(response["data"]["segments"][0]["stats"]["level"]["value"])
    trioRank = int(response["data"]["segments"][0]["stats"]["rankScore"]["value"])
    arenaRank = int(response["data"]["segments"][0]["stats"]["arenaRankScore"]["value"])

    timestamp = int(round(datetime.datetime.now().timestamp()))
    return {"status": res.status_code, "user_data": UserData(au, level, trioRank, arenaRank, timestamp)}

def postLevelUpdate(player_name: str, time: datetime.datetime, old_rank: int, new_rank: int) -> None:
    return requests.post(TINAX_API+"/level/register", json={
        'player_name': player_name,
        'timestamp': int(time.timestamp()),
        'old_rank': old_rank,
        'new_rank': new_rank
    })

def postRankUpdate(player_name: str, time: datetime.datetime, old_rank: int, old_rank_name: str, new_rank: int, new_rank_name: str, rank_type: str) -> None:
    return requests.post(TINAX_API+"/rank/register", json={
        'player_name': player_name,
        'timestamp': int(time.timestamp()),
        'old_rank': old_rank,
        'old_rank_name': old_rank_name,
        'new_rank': new_rank,
        'new_rank_name': new_rank_name,
        'rank_type': rank_type
    })
