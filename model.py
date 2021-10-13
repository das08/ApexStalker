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
    rank: int
    lastUpdate: int  # timestamp

    def __init__(self, au: ApexUser, rank: int, lastUpdate: int):
        self.au = au
        self.rank = rank
        self.lastUpdate = lastUpdate

    def __repr__(self):
        return f"AU: {self.au}, Rank: {self.rank}, Time: {self.lastUpdate}"
