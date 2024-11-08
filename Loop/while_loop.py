# Steps follow in While loop
# Start/Initialization
# Condition
# Increment/decrement

# write a program to print "Hello Universe! 10 times"?

i =1
while(i<11):
    print(i,"Hello Universe!")
    i = i+1 
print()

# write a program to print string in reverse Number?
a = 10
while(a>=1):
    print(a,"Smile")
    a = a-1
print()

# Assign the number in variable and show in the output screen.

a =0
while(a<5):
    print("x=" + str(a))
    a = a+1
print()

# Assign the number in variable and show in the output screen.

a =0
while(a<5):
    a = a+1
    print("x=" + str(a))
    
print()

# write a function with help of while loop
# and print the  attempt numbers?

def attempt(q):
    x =1
    while(x<=q):
        print("Attempt" +str(x))
        x = x+1
    print("Done!")

attempt(6)
print()
# Write aprogram to print the sum from 1 to 10 natural numbers
# with the help of while loop.

x=1
sum=0
while(x<11):
    sum= sum + x
    x = x+1
print(sum)
print()

# Write a program to print the product of the first 10 natural numbers?
x =1
mul = 1

while(x<11):
    mul = mul*x
    x=x+1
    print(mul)
print()