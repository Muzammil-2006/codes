a=int(input("Enter month number: "))
match a:
    case 1|3|5|7|8|10|12:
        print(f"{a} month has 31 days")
    case 4|6|9|11:
        print(f"{a} month has 30 days")
    case 2:
        print(f"{a} month has 28 or 29 days")    
