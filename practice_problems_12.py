# program to find the gcd of a number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

min_num = min(a, b)

while True:
    if a % min_num == 0 and b % min_num  == 0:
        gcd = min_num
        break
    min_num -= 1

print("GCD =", gcd)