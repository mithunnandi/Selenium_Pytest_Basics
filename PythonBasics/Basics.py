#Counter
from collections import Counter
a=[1,1,2,3,4,5,6,7,8]
c=Counter(a)
print(c)
print(list(c.elements()))

#Array pop
import array as arr
a=arr.array('i',[10,20,40])
print(a.pop())
print(a.pop(1))
a.remove(10)
print(a)

#Nested Dictionaries
emp_details={'Employee':{'Dave':{'ID':12345,'Salary':10000,'Designation':'Random'},
                         'Dave 1':{'ID':12346,'Salary':11000,'Designation':'Rand1om'}}}
print(emp_details)

#Dictionary to Dataframe
import pandas as pd
df=pd.DataFrame(emp_details['Employee'])
print(df)
 #identity operator
list_1=[10,20,30]
list_2=[10,20,20]
list_1 is list_2 #false
list_1 is not list_2 #true

#membership operator- checks if a element is present in an object
10 in list_1 #true
11 in list_1 #false

