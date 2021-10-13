import sys

from db import insert

args = sys.argv

insert("user_data",
       {"uid": args[1],
        "platform": args[2],
        "rank": int(args[3]),
        "last_update": 0
        }, upSert=True)
print(f"inserted user {args[1]}")