size=int(input("enter the size of your list:"))
x=[]
for i in range(size):
    element=int(input("Enter your numer:"))
    x.append(element)
for i in range(size):
    for j in range (size-i-1):
        if x[j]>x[j+1]:
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp

print("sorted array",x)