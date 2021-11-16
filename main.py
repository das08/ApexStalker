from discordwebhook import Discord
from db import insert, selectUID
from model import ApexUser, UserData
from network import fetchUserData, postRankUpdate
from settings import DISCORD_ENDPOINT
import datetime


def checkUpdate(au: ApexUser):
    discord = Discord(url=DISCORD_ENDPOINT)
    ud = fetchUserData(au)
    if ud["status"] == 200:
        newRecord: UserData
        oldRecord: UserData

        # Get oldRecord
        res = selectUID("user_data", "08das")

        userData = ud["user_data"]
        newRecord = userData
        insert("user_data",
               {"uid": userData.au.uid,
                "platform": userData.au.platform,
                "level": userData.level,
                "trio_rank": userData.trioRank,
                "arena_rank": userData.arenaRank,
                "last_update": userData.lastUpdate
                }, upSert=True)

        if len(res) != 0:
            oldRecord = UserData(userData.au, level=res[0][2], trioRank=res[0][3], arenaRank=res[0][4],
                                 lastUpdate=res[0][5])
            print("NR", newRecord)
            print("OR", oldRecord)
            hasUpdate = False
            messageFields = []
            if newRecord.lastUpdate > oldRecord.lastUpdate and newRecord.level > oldRecord.level:
                hasUpdate = True
                messageFields.append({"name": "レベル", "value": f"{oldRecord.level}→{newRecord.level}:laughing:"})
                print("level up")
                # discord.post(
                #     content=f"{newRecord.au.uid} のレベルが上がりました！ {oldRecord.level}→{newRecord.level} \N{SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES}")
                postRankUpdate(newRecord.au.uid, datetime.datetime.now(), oldRecord.level, newRecord.level)
            if newRecord.lastUpdate > oldRecord.lastUpdate and newRecord.trioRank != oldRecord.trioRank:
                hasUpdate = True
                messageFields.append({"name": "Trioランク", "value": f"{getRankTier(oldRecord.trioRank)}{oldRecord.trioRank}→{getRankTier(newRecord.trioRank)}{newRecord.trioRank}"})
                print("trio up")
            if newRecord.lastUpdate > oldRecord.lastUpdate and newRecord.arenaRank != oldRecord.arenaRank:
                hasUpdate = True
                messageFields.append({"name": "Trioランク", "value": f"{getRankTier(oldRecord.arenaRank)}{oldRecord.arenaRank}→{getRankTier(newRecord.arenaRank)}{newRecord.arenaRank}"})
                print("arena up")

            if hasUpdate:
                discord.post(
                    embeds=[
                        {
                            "author": {
                                "name": f"==== {newRecord.au.uid}の戦績変化 ====",
                            },
                            "fields": messageFields,
                        }
                    ],
                )


def getRankTier(rank: int):
    if rank < 1200:
        return "<:bronze:910106036197797938>"
    elif rank < 2800:
        return "<:silver:910102394275233832>"
    elif rank < 4800:
        return "<:gold:910106036051009556>"
    else:
        return "<:platinum:910106036055179294>"

def main():
    allUserList = []
    res = selectUID("user_data", "")
    for i in range(len(res)):
        uid, pf, level, trioRank, arenaRank, lu = res[i]
        allUserList.append(UserData(ApexUser(uid, pf), level, trioRank, arenaRank, lu))

    for i in range(len(allUserList)):
        checkUpdate(allUserList[i].au)


main()