n=int(input("enter a number"))
sum=0
while n!=0:
    a=n%10
    sum=(sum*10)+a
    n=n//10
print("reverse of number is ",sum)