
#Write a python script to find next prime number of a given number
n=int(input("enter the number : "))
j=n+1
while 1:
    f=0
    i=2
    while i<j:
        if j%i==0:
            f=1
            break
        i+=1
    if f==0:
        print(j)
        break     
    j=j+1
