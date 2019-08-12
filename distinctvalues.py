values=input("Enter the sequence of Numbers separated by comma: ")
list1=values.split(",")
l=[]
for i in list1:
    if list1.count(i):
        l.append(i)
print(set(l))
