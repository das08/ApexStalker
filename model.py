class ApexUser:
    uid: str
    platform: str

    def __init__(self, uid: str, platform: str):
        self.uid = uid
        self.platform = platform


class UserData:
    rank: int
    lastUpdate: int  # timestamp

    def __init__(self, rank: int, lastUpdate: int):
        self.rank = rank
        self.lastUpdate = lastUpdate
