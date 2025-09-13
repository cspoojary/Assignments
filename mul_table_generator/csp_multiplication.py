"""Multiplication Table Generator
Input a number and print its multiplication table up to 10."""

n = int (input("Enter the number:"))

for i in range(1,11):
    print(n ,"x", i ,"=", n*i)