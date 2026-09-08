a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
op=input("Enter operator(+,-,*,/): ")
match op:
    case "+":
        print("Result=",a+b)
    case "*":
        print("Result=",a*b)  
    case "-":
        print("Result=",a-b) 
    case "/":
        if b!=0:
            print("Result=",a/b) 
        else:
            print("Cannot be divisible by 0")
    case _:
        print("Invalid operator")                   
    