def options():
    print("SIMPLE CALCULATOR")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. stop")
    
    Operation = int(input("Enter any number operation(1/2/3/4/5): "))
        
    if Operation > 5 or Operation < 1:
        print("Invalid,Try once again")
        options()
 

    if(Operation != 5):
        num1 = float(input("Enter the first value:"))
        num2 = float(input("Enter the second value:"))
    else:
        print("The calculation ended")
        return 0
    
    match Operation:
        case 1:
            print("The sum of the two number is:",num1+num2)
            options()
        case 2:
            print("The difference of the number is:", num1-num2)
            options()
        case 3:
            print("The product of two number is:",num1*num2)
            options()
        case 4:
            if num1 == 0 or num2 == 0:
                print("The value are inavlid")
                options()
            print("The Quotient of the two number is :", num1 /num2)
            options()

options()