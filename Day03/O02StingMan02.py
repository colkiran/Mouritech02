
# maketrans, translate
print("maketrans".center(40, "-"))
st = "hello world"
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'                       # length of a and b should be the same
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")          # dictionary

print("Translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")
print(f"st :{st}")
