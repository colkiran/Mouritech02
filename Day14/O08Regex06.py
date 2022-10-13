
import re

# st = "best"
# res = re.search(r'b(oa|es)t', st)

st = "sample.py"

res = re.search(r'\.py$', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")
