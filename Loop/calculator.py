# We are Making the calculator by using control statements and this 
# calucalot provide basic solutions to user.

print(
  '''
+ Addition
- Substraction
* Multiplication
/ Division

'''
)

# we use evel type cast technique to handle 
# all types of values like int,float, binary.

num1 = eval(input("Enter the value 1: "))
num2  = eval(input("Enter the value 2: "))
opr = input("Enter the the Operation...(+,-,*,/)")

if opr == "+":
    print(num1+num2)
elif opr =="-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
else:
    print("Invalid Operation...")


