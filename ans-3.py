#Write a python script to print all Prime numbers under 100
n=1
while n<100:
    j=2
    f=0
    while j<n:
        if n%j==0:
            f=1
            break
        j=j+1
    if f==0:    
        print(n,end=' ')   
    n+=1 
