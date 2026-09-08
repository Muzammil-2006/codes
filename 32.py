a=int(input("Enter a number: "))
if a>0:
    print("Positive")
    if a%2==0:
        print("Even")
    else:
        print("Odd")
elif a<0:
    print("Nagative")
else:
    print("Zero")                