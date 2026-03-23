# program to create dictionary of hindi words with their english neanings 

words={
    "Dhanyavadh":"Thankyou",
    "Kush":"Happy",
    "Dukh":"Sad",
    "Dukan":"Shop"
}
print(type(words))
print(words)


# program to input six numbers from the user and display all the unique nunmbers once

numbers=set()
num1=int(input("enter number 1 : "))
numbers.add(num1)
num2=int(input("enter number 2 : "))
numbers.add(num2)
num3=int(input("enter number 3 : "))
numbers.add(num3)
num4=int(input("enter number 4 : "))
numbers.add(num4)
num5=int(input("enter number 5 : "))
numbers.add(num5)
num6=int(input("enter number 6 : "))
numbers.add(num6)
print(numbers)


# program to perform set operations

s={69,90,70,60,10}
s1={2,3,4,60,90}
print(s)
s.add(22)                # add operation 
print("after adding 22")
print(s)

ans=s.intersection(s1)   # intersection operation
print("after intersecting s and s1")
print(ans)

print("after union of s and s1")
ans1=s.union(s1)         # union operation
print(ans1)


# properties of Dictionaries and Sets

print("Dictionaries are indexed and allow duplicate values whereas Sets are unindexed and cannot allow duplicate values ")
