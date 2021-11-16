class ApexUser:
    uid: str
    platform: str

    def __init__(self, uid: str, platform: str):
        self.uid = uid
        self.platform = platform

    def __repr__(self):
        return f"User: {self.uid}, PF: {self.platform}"


class UserData:
    au: ApexUser
    level: int
    trioRank: int
    arenaRank: int
    lastUpdate: int  # timestamp

    def __init__(self, au: ApexUser, level: int, trioRank: int, arenaRank: int, lastUpdate: int):
        self.au = au
        self.level = level
        self.trioRank = trioRank
        self.arenaRank = arenaRank
        self.lastUpdate = lastUpdate

    def __repr__(self):
        return f"AU: {self.au}, Level: {self.level}, trioRank: {self.trioRank}, arenaRank: {self.arenaRank}, Time: {self.lastUpdate}"
