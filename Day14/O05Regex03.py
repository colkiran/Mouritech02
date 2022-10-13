
import re

st = "baaaaaat"

# res = re.search(r'ba*t', st)
# res = re.search(r'ba?t', st)
res = re.search(r'ba+t', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")
