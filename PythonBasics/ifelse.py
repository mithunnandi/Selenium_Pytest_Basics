a=int(input("please enter"))

if (a>0):
    print("number is positive")
elif a<0:
    print("number is smaller than 0")
elif a==0:
    print("number is equal to zero")

if True:
    print("PASS")
else:
    print("FAIL")

w,x,y,z=100,200,3000,400

if (w>x and w>y and w>z) :
    print("w is the highest no.")
elif(x>y and x>z):
    print("x is highest")
elif(y>z and y>w):
    print("y is highest")
else:
    print("z")

total = int(input("Enter the value"))
if(total<100):
    total=total+20
elif(total>=100 and total<=500):
    total=total+50
else:
    total=total+100

print(total)
print("total="+str(total))