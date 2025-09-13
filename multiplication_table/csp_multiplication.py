"""Multiplication Table Generator
Input a number and print its multiplication table up to 10."""

while True:
    number = input("Enter the number:")

    try:
        n = int(number)
        print(f"Here is {n}th multiplication table:")
        for i in range(1,11):
            print(n ,"x", i ,"=", n*i)
        break

    except(ValueError):
        print("ValueError")
        

