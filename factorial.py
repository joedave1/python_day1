n=int(input("Enter the Number to find Factorial value:"))
if n==0:
    print("The factorial value is ",1)
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial value is ",fact)
