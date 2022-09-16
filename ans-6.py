#Write a python script to print first N prime numbers
n=int(input("enter the value of  n : "))
c=0
j=1
while 1:
    f=0
    i=2
    while i<j:
        if j%i==0:
            f=1
            break
        i+=1
    if f==0:
        print(j,end=' ') 
        c=c+1
    if c==n:
        break       
    j=j+1