import sys

from db import delete

args = sys.argv

delete("user_data",
       args[1])
print(f"deleted user {args[1]}")