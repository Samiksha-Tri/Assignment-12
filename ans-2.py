#Write a python script to check whether a given number is Prime or not
n=int(input("enter a number : "))
c=0
i=1
while i<=n:
    if n%i==0:
        c=c+1
    i+=1    
if c==2:
    print("its prime number")
else:
    print("its not prime number")
          
