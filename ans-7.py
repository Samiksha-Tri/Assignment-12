#Write a python script to check whether a given pair of numbers are co-Prime
#numbers or not.

n1=int(input("enter first number : "))
n2=int(input("enter second number : "))
for i in range(2,n1+1):
    if n1%i==0 and n2%i==0:
        print("not co-prime")
        break
else:
    print("co-prime")        