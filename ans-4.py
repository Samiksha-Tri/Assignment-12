#Write a python script to print all Prime numbers between two given numbers (both
#values inclusive)

n1=int(input("enter first number : "))
n2=int(input("enter second number : "))
while n1<=n2:
    j=2
    f=0
    while j<n1:
        if n1%j==0:
            f=1
            break
        j=j+1
    if f==0:    
        print(n1,end=' ')   
    n1+=1 


