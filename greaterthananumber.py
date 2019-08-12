values=input("Enter the sequence of Number separated by comma:")
list1=values.split(",")
key=input("Enter the value to check greater in the list: ")
print("These are the numbers in the list greater than key:")
for i in list1:
    if i>key:
        print(i)
