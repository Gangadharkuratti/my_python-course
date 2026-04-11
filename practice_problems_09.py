# program to print whether a given number is prime

num=int(input("enter number : "))
count=0
for i in range(2,num):
    if num%i==0:
        count+=1
if  count==0:
    print("prime number")
else:
    print("not a prime number")           


# program to find wheher a given number  is perfect or not

num=int(input("enter number : "))

sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print("perfect number")
else:
    print("not a perfect number")            