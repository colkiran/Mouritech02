
# def get_name(surname):
#     print(f"surname is {surname}")
#
#     while True:
#         name = yield                    # accepts values from user
#         print(f"received {name}")
#         print("-" * 40)
#         if surname in name:
#             print(f"surname {surname} found in {name}")

def get_name(surname):
    print(f" surname is {surname}")

    while True:
        name = yield
        print(f" received {name}")
        print("-" * 40)
        if surname in name:
            print(f"surname found: {surname} in {name}")

coObj = get_name("Pillai")
print(coObj)
coObj.__next__()
coObj.send("Sachin Tendulkar")
coObj.send("Virat Kholi")
coObj.send("Dhanraj Pillai")
