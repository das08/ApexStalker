from discordwebhook import Discord
from db import insert, selectUID
from model import ApexUser, UserData
from network import fetchUserData, postLevelUpdate, postRankUpdate
from settings import DISCORD_ENDPOINT
import datetime


def checkUpdate(au: ApexUser):
    discord = Discord(url=DISCORD_ENDPOINT)
    ud = fetchUserData(au)
    if ud["status"] == 200 and ud["user_data"] is not None:
        newRecord: UserData
        oldRecord: UserData

        # Get oldRecord
        res = selectUID("user_data", au.uid)

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
                try:
                    postLevelUpdate(newRecord.au.uid, datetime.datetime.now(), oldRecord.level, newRecord.level)
                except:
                    print("error tinax api (level)")
            if newRecord.lastUpdate > oldRecord.lastUpdate and newRecord.trioRank != oldRecord.trioRank:
                hasUpdate = True
                messageFields.append({"name": "トリオRank", "value": f"{getRankTier(oldRecord.trioRank)}{oldRecord.trioRank}→{getRankTier(newRecord.trioRank)}{newRecord.trioRank}  {getRankDiff(oldRecord.trioRank, newRecord.trioRank)}"})
                print("trio up")
                try:
                    postRankUpdate(newRecord.au.uid, datetime.datetime.now(), oldRecord.trioRank, getRankName(oldRecord.trioRank), newRecord.trioRank, getRankName(newRecord.trioRank), 'trio')
                except:
                    print('error tinax api (trio rank)')
            if newRecord.lastUpdate > oldRecord.lastUpdate and newRecord.arenaRank != oldRecord.arenaRank:
                hasUpdate = True
                messageFields.append({"name": "アリーナRank", "value": f"{getArenaRankTier(oldRecord.arenaRank)}{oldRecord.arenaRank}→{getArenaRankTier(newRecord.arenaRank)}{newRecord.arenaRank}  {getRankDiff(oldRecord.arenaRank, newRecord.arenaRank)}"})
                print("arena up")
                try:
                    postRankUpdate(newRecord.au.uid, datetime.datetime.now(), oldRecord.arenaRank, getRankName(oldRecord.arenaRank), newRecord.arenaRank, getRankName(newRecord.arenaRank), 'arena')
                except:
                    print('error tinax api (arena rank)')

            if hasUpdate:
                messageFields[-1]["value"] += "\n\n [グラフを見る](https://oneapex.tinax.work/web/level)"
                discord.post(
                    embeds=[
                        {
                            "title": f"\N{Confetti Ball} {newRecord.au.uid}の戦績変化 \N{Party Popper}\n",
                            "fields": messageFields,
                        }
                    ],
                )


def getRankTier(rank: int):
    if rank < 1200:
        return "<:bronze:910108271828942848>"
    elif rank < 2800:
        return "<:silver:910108271396921396>"
    elif rank < 4800:
        return "<:gold:910108271577296947>"
    else:
        return "<:platinum:910108271682138112>"

def getArenaRankTier(rank: int):
    if rank < 1600:
        return "<:bronze:910108271828942848>"
    elif rank < 3200:
        return "<:silver:910108271396921396>"
    elif rank < 4800:
        return "<:gold:910108271577296947>"
    else:
        return "<:platinum:910108271682138112>"

def getRankName(rank: int) -> str:
    if rank < 1200:
        return "bronze"
    elif rank < 2800:
        return "silver"
    elif rank < 4800:
        return "gold"
    else:
        return "platinum"

def getRankDiff(old: int, new: int):
    rankDiff = new - old
    if rankDiff < 0:
        return f"({rankDiff})"
    else:
        return f"(+{rankDiff})"

def main():
    allUserList = []
    res = selectUID("user_data", "")
    for i in range(len(res)):
        uid, pf, level, trioRank, arenaRank, lu = res[i]
        allUserList.append(UserData(ApexUser(uid, pf), level, trioRank, arenaRank, lu))

    for i in range(len(allUserList)):
        checkUpdate(allUserList[i].au)


main()
