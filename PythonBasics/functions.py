print("***without parameters*****")
def test():
    print("returning")

test()


print("*** with parameters*****")
def test(a):
    print("returning \t"+ str(a))

test(10)

def test(a):
    print("returning \t"+ str(a))
    print(a*10)

test(10)

print("\n *** Optional/ default parameter***")
def fun(name="india"):
    print("the name is \t" +str(name))
fun()


def fun(name="England"):
    print("the name is \t" +str(name))
fun("West Indies")

print("*** passing a list to a function ***")
def fetchlist(list):
    print(list)

#names=["Python","Java","C"]
fetchlist(["Python","Java","C"])

def fetch(list1):
    for i in list1:
        print(i)

names=["Python","Java","C++"]
fetch(names)

print("** with return type**")
def sum(a,b,c):
      e=a+b+c
      return e
e1= sum(1,2,3)
print(e1)

def getcapital(country):
    if country == "India":
       return "DElhi"
    else:
        return "sorry!!"
print(getcapital("India"))
print(getcapital("USA"))

def launchbrowser(browsername):
    if browsername == "chrome":
       return "Launching CHROME"
    elif browsername == "Firefox":
        return "launching FireFox"
    else:
        return "Try again !!"
print(launchbrowser("chrome"))
print(launchbrowser("UER"))


def factorial(num):
    if(num>1):
        num=num*factorial(num-1)
    return num
print(factorial(4))



def login(username,password):
    print("login with %s and %s"%(username,password))

login("test11@gmail.com","test@123")
login(username="testing@yahoo.com",password="abc")

def multipleargs(*arg):
    for x in arg:
        print(arg)
multipleargs(10,20,30,40)

cube =lambda a:a**4 # a to the power of 4
print(cube(2))


