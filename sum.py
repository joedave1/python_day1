def Summation(a,b,c):
    if a==b and a==c:
        return (a+b+c)*3
    else:
        return (a+b+c)
x=int(input("Enter the First Number :"))
y=int(input("Enter the second Number :"))
z=int(input("Enter the Thrid Number :"))
print(Summation(x,y,z))
