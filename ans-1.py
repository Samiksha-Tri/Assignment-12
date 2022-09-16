#Write a python script to reverse a number.
n=int(input("enter a number : "))
while n>0:
    rem=n%10
    print(rem,end='')
    n=n//10
    