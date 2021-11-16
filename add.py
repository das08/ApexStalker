import sys

from db import insert

args = sys.argv

insert("user_data",
       {"uid": args[1],
        "platform": args[2],
        "level": int(args[3]),
        "trio_rank": int(args[4]),
        "arena_rank": int(args[5]),
        "last_update": 0
        }, upSert=True)
print(f"inserted user {args[1]}")