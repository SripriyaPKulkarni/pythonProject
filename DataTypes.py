#List
#List is a datatype that allows multiple values and can be different data types
values=[1,2,"priya",4.5,8]
print(values[1])

#to print last value
print(values[-1])

#To get sublist
print(values[1:3])

#inserting
values.insert(3,"Kulkarni")

print(values)

#adding /appending
values.append("Hello")

print(values)

#updating
values[1]="PRIYA"

print(values)

#deleting
del values[1]

print(values)

#Tuple data type
#Tuple is immutable, we cannot update

a=(1,2,3,4)

print(a)

#Dictionary---Key value pair
dic={"a":1, 4:"bcd","c":"Hello World"}

print(dic)

print(dic[4])

print(dic["c"])

dic["first name"]="Madhu"

print(dic)