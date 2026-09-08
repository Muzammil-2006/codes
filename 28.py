a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
if a==b and b==c:
    print("Equalateral tringle")
elif a==b or b==c or a==c:
    print("Isosceles tringle")
else:
    print("Scalene tringle")        