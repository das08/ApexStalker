from discordwebhook import Discord
from db import insert, selectUID
from model import ApexUser, UserData
from network import fetchUserData
from settings import DISCORD_ENDPOINT


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
                "rank": userData.rank,
                "last_update": userData.lastUpdate
                }, upSert=True)

        if len(res) != 0:
            oldRecord = UserData(userData.au, rank=res[0][2], lastUpdate=res[0][3])
            # oldRecord.lastUpdate = 1634124350
            # oldRecord.rank = 170
            print("NR", newRecord)
            print("OR", oldRecord)
            if newRecord.lastUpdate > oldRecord.lastUpdate and newRecord.rank > oldRecord.rank:
                print("posted")
                discord.post(
                    content=f"{newRecord.au.uid} のランクが上がりました！ {oldRecord.rank}→{newRecord.rank} \N{SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES}")


def main():
    allUserList = []
    res = selectUID("user_data", "")
    for i in range(len(res)):
        uid, pf, rank, lu = res[i]
        allUserList.append(UserData(ApexUser(uid, pf), rank, lu))

    for i in range(len(allUserList)):
        checkUpdate(allUserList[i].au)


main()
