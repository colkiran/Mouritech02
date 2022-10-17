
import re

st = "the quick brown fox jumps over the lazy dog."

res = re.search('j\w+', st)

if res:
    print("Match found.....")
    print(f"String that dindt match regex :{st[:res.start()]}")
    print(f"String that matched our regex :{res.group(0)}")
    print(f"String that is yet to be checked :{st[res.end():]}")
else:
    print("Match not found.....")