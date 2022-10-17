
import re

st = ["2020 olympics games have @# been cancelled",
     "Dr. Vikram Sarabhai was +%--the ISRO's first chairman",
     "Dr. Abdul       kalam the father       of india's missile program"]

for i in range(len(st)):

     st[i] = re.sub(r'\W', " ", st[i])

     st[i] = re.sub(r'\d', " ", st[i])

     st[i] = re.sub(r"\s+", " ", st[i])

for i in range(len(st)):
     print(st[i])