
class MyStr(str):
    def Append(self, st):
        return st + self

    def upper(self):
        pass

    def lower(self):
        pass

    def isupper(self):
        pass

    def isalpha(self):
        pass


st = MyStr("Yuvraj")
print(st.Append("Mr."))


class MyListClass(list):

    def append(self, object):
        print("Record :",object)
        super().append(object)


t1 = MyListClass()
print(f"t1 :{t1}")
t1.append("apples")
t1.append('grapes')
t1.append('mangoes')

print(f"t1 :{t1}")