name="Maschreanas Sharma"
for i in range(len(name)):
    print(name[i])
    if(name[i]=='a'):
        print("FOUND a")
        break

name="VICTORIA DHANWANTARI"
for i in range(len(name)):
    print(name[i])
    if(name[i]=='A'):
        print("FOUND a")
        continue

Country=["Vienna","England","Bhutan","Nepal"]
for i in range(4):
    print(Country[i])
    if(Country[i]=='Bhutan'):
        print("Bhutan mil gaya")
        break


City=["Vatican","Egmore","kathmandu","mizoram"]
flag=False
for i in range(len(City)):
    print(City[i])
    if(City[i]=='Egmore'):
        print("Egmore mil gaya")
        flag= True
        break
if(flag):
         print("Lets go there")