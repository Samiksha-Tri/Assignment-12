#Write a python script to print first N terms of a Fibonacci series
n=int(input("enter the value of n"))
x=0
y=1
print(x,y,end=' ')
i=2
while i<n:
    z=x+y
    print(z,end=' ')
    x=y
    y=z
    i+=1

