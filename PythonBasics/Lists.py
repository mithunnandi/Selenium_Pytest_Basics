score=[10, 20, 'thirty', 30.4, 50]
print(score)
print(score[2])
print(score[-2])
print(score[1:4])

a=score[:] # Creating Copy
print(a)
print(a+[10,20,"Learning"])

b=a+[2,20,45]
print(b)
b.append(2**3)
print(b)
# b[:] =[] empties the string
#Print(b)