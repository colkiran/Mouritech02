
import re

# url = "www.google.com / search='%new hindi movies?' % / get_data2019 / fetch_data frm_1 / imdb? %hindi%movies$& / result = page1.aspx"
#
# while (re.search(r'/', url)):
#     res = re.search(r'/', url)
#     print(f"{url[:res.start()]}")
#     url = url[res.end():]
#
# print(url)


FL = open("story.txt", "r")
st = FL.readlines()
val = 0
for line in st:
   if(re.search(r'\b[aeiou]\w*', line)):
      print(re.search(r'\b[aeiou]\w*', line).group(0))
      val = val + 1
print('Count of words that start with vowels:',val)