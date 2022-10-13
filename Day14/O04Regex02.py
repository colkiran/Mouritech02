
import re

st = "the quick brown fox jumps over the lazy dog"

# res = re.match(r'^the', st)
# match - will work only at the beginning of the string

res = re.search(r'dog$', st)


if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")
