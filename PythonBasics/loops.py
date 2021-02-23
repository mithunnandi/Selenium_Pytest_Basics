#While Loop

i=0
while(i<10):
    print(i)
    i=i+1

print("**while with else***")

j=0
while(j<=4):
    print("printing J \t"+ str(j))
    j=j+1
else:
    print("exiting")

print("*******For Loop*******")
lang=["c","java","C++","Python"]
for i in lang:
    print(i)

String=("PYTHON SIKH RAHA HOON !!")
for i in String:
    print(i)
print("**ITERATING THORUGH THE COMPLETE LIST USING RANGE FUNCTION**")

str1=["Hindi","English","Maths"]
for i in range(len(str1)):
    print((str1[i]))
else:
    print("Completed iteration")

print("**ITERATING THORUGH THE specific elements LIST USING RANGE FUNCTION**")

str2=["Hin","Eng","Mat","Sci"]
for i in range(2):
    print((str2[i]))
else:
    print("Completed iteration")

print("*******For Loop with Else *******")
Country=["canada","japan","Cambodia","Peru"]
for i in Country:
    print(i)
else:
    print("Khatam !! TATA !! GOODBYE")

print("NESTED LOOP -NUMBER PATTERN")
for i in range(1,5):
    for j in range(i):
        print(i, end='')
    print()