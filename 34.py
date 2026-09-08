import cmath
a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
c=int(input("Enter third num: "))
D=b*b-4*a*c
if D>0:
    root1=(-b+D**0.5)/(2*a)
    root2=(-b-D**0.5)/(2*a)
    print("The roots are real and different")
    print("Root 1=",root1)
    print("Root 2=",root2)
elif D==0:
    root=-b/(2*a)
    print("Real and equal roots")
    print("Root 1=Root 2=",root)
else:
    root1=(-b+cmath.sqrt(D))/(2*a)
    root2=(-b-cmath.sqrt(D))/(2*a)
    print("Imaginary/comlex roots")
    print("Root 1=",root1)
    print("Root 2=",root2)
