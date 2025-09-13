def multi():
    try:
        n=int(input("enter the num: "))
        print(f"multiplication table of {n} : ")
        for i in range(1,11):
            k=n*i
            print(f"{n} * {i} = {k}")
        
    except(ValueError):
        print("invalid input ")
        multi()        

multi()        