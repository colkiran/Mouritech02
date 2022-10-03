
def greet():
    print("Greetings Mr.Sachin, welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# city is a default variable, gname is a non default variable
def greetGstCty(gname,  city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.....")

greet()
print("-" * 40)

greetGst("Sachin")
greetGst("Rahul")

print("-" * 40)

greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Azhar", "Hyderabad")

print("-" * 40)
# Function Args
def admisn(name, dob, gender, contno, mrst, qlf, adr, city):
    print(f"Name           :{name}")
    print(f"DOB            :{dob}")
    print(f"Gender         :{gender}")
    print(f"Contact No.    :{contno}")
    print(f"Marital Status :{mrst}")
    print(f"Qualification  :{qlf}")
    print(f"Address        :{adr}")
    print(f"City           :{city}")
    print("-" * 40)

# *args - list
admisn("Jack", "04/07/1981", "Male", "23098234", "Married", 'Bcom', "Indiranagar 12th main", "Bangalore")

# **kwargs - dictionary (named Args)
admisn(dob="08/10/1983", qlf='MBA', adr="Jaynagar, 4th block", name='Gracy', gender="Female", city="Bangalore", contno="20340234", mrst="Married")

# Variable length Args
print("-" * 40)
def multiMe(*numbers):              # accepts more than one number
    print(numbers)
    print(*numbers)                 # unpacking
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(multiMe(1, 2, 3, 4, 5))

print("-" * 40)
# accepting like a dictionary
def extract_details(**details):
    print(details)
    for k in details:
        print(k, "=>", details[k])


extract_details(name="sachin", runs=120, oppn="WI", venue="Sabina Park")

print("-" * 40)
# functions can return values
# supports recursion
# using recursion find  - factorial of a number, fibanocci series
def fact(n):
    if n <= 1:
       return 1
    else:
       return n * fact(n-1)

n = 5
print(f"The factorial of {n} is :{fact(n)}")

print("-" * 40)

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10
print("Fibonacci sequence:")
for i in range(nterms):
    print(recur_fibo(i), end=" ")
print()

print("-" * 40)
def Arithmetic_calc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

print(Arithmetic_calc(20, 6))

print("-" * 40)
# doc strings
def fun():
    #this is a comment
    "This is a doc string"
    print("Hello World..")

fun()
print(fun.__doc__)

print("-" * 40)
def fun1(x, y):
    """
    fun1(x, y)

    function fun1 takes two args
    1. if both the args are integers then the results are sum of both the numbers
    2. if both the args are strings then the results are a concatenation of both strings
    """
    return x + y

print(fun1(20,10))
print(fun1('hello', "world"))

print("-" * 40)
help(fun1)