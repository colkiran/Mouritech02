
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 40)
print(f"st[0]  :{st[0]}")                        # strings are stored like lists
print(f"st[6]  :{st[6]}")
print(f"st[10] :{st[10]}")
print("-" * 40)
# slicing
print(f"st[0:5]   :{st[0:5]}")
print(f"st[6:11]  :{st[6:11]}")
print(f"st[0:11]  :{st[0:11]}")
print(f"st[0:]    :{st[0:]}")
print(f"st[:11]   :{st[:11]}")
print(f"st[:]     :{st[:]}")

print("-" * 40)
# reverse indexing
print(f"st :{st}")
print(f'st[-1]  :{st[-1]}')
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 40)
# reverse slicing
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 40)
st = "malayalam"
print(st[:] == st[::-1])

print("-" * 40)
# Strings are immutable
st = "hello world"
print(f"st[6] :{st[6]}")
# st[6] = "W"

print("-" * 40)
# print(dir(st))

st = "hello world"
st1 = "the quick brown fox jumps over the lazy dog"

print("find".center(40, "-"))
print(f"st :{st}")

pos = st.find("l")
print(f"pos :{pos}")

pos = st.find("l", st.find("l") + 1)
print(f"pos :{pos}")

pos = st.find("l", st.find("l", st.find("l") + 1) + 1)
print(f"pos :{pos}")

print("-" * 40)

print(f"st1 :{st1}")

pos = st1.find("the")
print(f"pos :{pos}")

pos = st1.find("the", st1.find("the") + 1)
print(f"pos :{pos}")

print("replace".center(40, "-"))
print(f"st :{st}")

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

print("-" * 40)

print(f"st :{st}")
res = st.upper()
print(f"res :{res}")
res1 = res.lower()
print(f"res1 :{res1}")

res = st.title()
print(f"res :{res}")
print(res.swapcase())

print(len(st))
print(st.index("w"))
print(st.count("l"))

print("-" * 40)
gname = "Sachin"
res = f"Hello Mr.{gname}"               # interpolation
print(res)

print("hello %s" % ("Rahul"))
print("hello {}".format("Rahul"))
