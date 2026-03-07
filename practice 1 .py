''''program for adding two numbers'
first = input("enter first number:")
second = input ("enter second number:")
sum = int(first) + int(second) 
print (sum) 
 iska abhi concatination hua hai kyunki we didnt do its type conversion 
type conversion ke liye bas int add krdenge or dono values ke saath alag alag int use krna hoga 

'''

'Strings'
name = "Tony Stark"

print(name.upper())
print(name)

'find operation in string '
name = "Tony Stark"
print(name.find("S"))  
print(name.find("p"))

'''abh ye upper find operation is used to tell the index value of of the alphabet
agar wo alphabet is not present in the string it returns -1'''

'Replace operation'
name = "Bat man"
print(name.replace("Bat man","Ironman"))
'''we can replace character ,word string etc'''
print('t'in name)
