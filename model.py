class ApexUser:
    uid: str
    platform: str

    def __init__(self, uid: str, platform: str):
        self.uid = uid
        self.platform = platform


class UserData:
    au: ApexUser
    rank: int
    lastUpdate: int  # timestamp

    def __init__(self, au: ApexUser, rank: int, lastUpdate: int):
        self.au = au
        self.rank = rank
        self.lastUpdate = lastUpdate
