a=100
print(a)

#Strings
s1='Testing Python'
print(s1[2])
print("hello \n world")
print("hello \t world")
print("hello \t world\t" *5)

print("Python" in s1)
print("P1"not in s1)
print("my name is %s and my age is %i" %("Mithun",20))  #Formatting operator

s3='''Hi All I am learning python and want to print this statement in triple  single quotes'''
print(s3)

s3='''Hi All I am learning python and want to print this statement in triple  double quotes'''
print(s3)

print('Hi I\'m learning literals')
print("Was just trying a statement within double \"quotes\"")

s5="this is a part of learning and I am learning"
print(s5)
print(s5.capitalize())
print(s5.count("learning")) # Counts the occurence of a word in the string
print(s5.find("a")) # returns the position of the word in the string
print(len(s5))
print(s5.lower())
print(s5.upper())

#Trimming a string
s6=" hello "
print(s6.lstrip())
print(s6.rstrip())

print(s6.replace(" hello ","HI"))

s7="Hello World Oye Hello !! Hello Abe "
print(s7.split("Hello"))

#Comparison
a="test"
b="test"
print(a is  b)
print(a==b)