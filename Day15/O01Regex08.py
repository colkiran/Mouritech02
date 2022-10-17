
import re

st = "this is a samples ampled string"

# res = re.search(r'\w+', st)
# res = re.search(r'\W+', st)
# res = re.search(r'\d+', st)
# res = re.search(r'\D+', st)
# res = re.search(r'\s+', st)
# res = re.search(r'\S+', st)
# res = re.search(r'(\ba\w+)', st)
# res = re.search(r'(\Ba\w+)', st)
# res = re.search(r'\Athis', st)

res = re.search(r'string\Z', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")
