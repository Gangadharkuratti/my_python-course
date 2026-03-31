# program to find whether the entered number is positive negative or zero

num=int(input("enter number : "))
if num<0:
    print("the number entered is negative")
elif num>0:
    print("the number entered is positive")
elif num==0:
    print("the numbere entered is zero")
else:
    print("invalid number")            



# program to find the largest of two numbers

num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))

if num1>num2:
    print("number one is greater ")
else:
    print("number two is greater")    


# program to find the largest of three numbers


num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))
num3=int(input("enter number 3 : "))

if num1>num2 and num1>num3:
    print("number one is greater")
elif num2>num1 and num2>num3:
    print("number two is greater")
else:
    print("number three is greater")  


# program to swap two numbers

num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))

print(num1,num2)

num1,num2=num2,num1
print("after swapping")

print(num1,num2)


# program to swap two numbers using third variable


num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))

print(num1,num2)

a=num1
num1=num2
num2=a
print("after swapping")
print(num1,num2)

