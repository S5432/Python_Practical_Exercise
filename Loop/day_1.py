# 1. Print the first N natural numbers by using the for loop?
# Logic: we now that between 0 to 10 we have 11 numbers
# natural numbers start from 1 so we give range for 1 to 11.

n= 11

for i in range(1,n):
    print(i)
print()

# 2. Print the Natural numbers  by enter the given range from the users?
'''
x = int(input("Enter the Strating number:"))
y = int(input("Enter the Ending Number:"))
# m =n+1
for i in range(x,m):

for i in range(x,y):
    print(i)
print()
'''

# 3. write a program to print all the even numbers within the given range.
'''
x = int(input("Enter the Strating number:"))
y = int(input("Enter the Ending Number:"))
m =y+1
for i in range(x,m):
    if i%2==0:
        print(i)
print()

'''

#4.Write a Python program to calculate the sum of all the numbers from 1 to a given range.?
n = int(input("Entera number:"))
a =1
sum=0
while(a<=n):
    sum += a
    a += 1
print(sum)
print()

'''
# by using for loop
# by for loop
x = int(input("Enter the number:"))
y=1
n = x+1
sum=0
for i in range(y,n):
  sum = sum+i
print(sum)
'''

# 5 Write a python program to print the multiplication table of a given number?

m = int(input("Enter a number:"))
for i in range(1,11):
    print(m,"*",i,"=", m*i)