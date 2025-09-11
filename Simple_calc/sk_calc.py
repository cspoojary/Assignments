
def arithmetic_operations():
    
    ch=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.exit\nEnter your choice: "))
    
    if ch > 5 or ch < 1:
        print("Invalid,Try once again")
        arithmetic_operations()
        
    if ch!=5:
     a= int(input("Enter a value: "))
     b= int(input("Enter b value: "))
    else:
        print("your exited from the program")
        exit()   
    if ch==1:
        print("Addition is:",a+b)
        arithmetic_operations()
    elif ch==2:
        print("Subtraction is:",a-b) 
        arithmetic_operations()   
    elif ch==3:
        print("Multiplication is:",a*b)
        arithmetic_operations()
    elif ch==4:
        if b!=0:
            print("Division is:",a/b)
            arithmetic_operations()
        else:
            print("Division by zero not allowed")
            arithmetic_operations()
    
    
        
        

arithmetic_operations()

