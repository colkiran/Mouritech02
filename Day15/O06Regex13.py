
import re

st = "the quick brown fox jumps over the lazy dog."

res = re.sub(r'(t\w+)', 'The', st, 1)

print(f"res :{res}")

print("-" * 40)



