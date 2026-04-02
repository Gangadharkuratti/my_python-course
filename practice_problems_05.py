 # program to check whether a user entered character is vowel or a consonent

ch=input("enter character : ")
if (ch>="a" and ch<="z") or (ch>="A" and ch<="Z"):
    if ch  in "aieouAEIOU":
        print("entered character is vowel")
    else:
        print("entered character is a consonent")
else:
    print("entered character is not a alphabet")     


# program to check the entered alphabet is a lower or upper case

alph=input("enter alphabet : ")
if len(alph)==1 and alph.isalpha():
     if "A" <= alph <="Z":
      print("entered alphabet is upper case")
     elif "a"<= alph <="z":
      print("entered alphabet is lower case") 
else:
    print("you have entered a wrong alphabet")

# program to print the ASCII value of entered character


alph=input("enter alphabet : ")
if len(alph)==1 and alph.isalpha():
   print("ASCII value of entered alphabet is ",ord(alph))
else:
   print("invalid input (enter single alphabet only)")

# program to print the sum of natural numbers


num=int(input("enter number : "))

sum=0
for i in range(1,num+1):
 sum=sum+i
print("sum is : ",sum) 

