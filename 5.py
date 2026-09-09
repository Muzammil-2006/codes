n=int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print("divisible by both 3 and 5")
elif n%3==0:
    print("divisible by 3")    
elif n%5==0:
    print("divisible by 5")
else:
    print("divisible by nither 3 nor 5")        