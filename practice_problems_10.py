# program to print the armstrong number

num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp =temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# program to find the pallindrome number

num = int(input("Enter number: "))
temp = num
rev = 0

while temp > 0:
    d = temp % 10
    rev = rev * 10 + d
    temp = temp // 10

if rev == num:
    print("Palindrome")
else:
    print("Not Palindrome")
