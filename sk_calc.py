# a=2
# b=3
# print(a&b)
# print(~2)
# print(2>>3)
# print(2<<3)

  
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

print("\nArithmetic Operation")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)   
if(b != 0):
    print("a / b =", a / b)
    print("a % b =", a % b)
    print("a // b =", a // b)
else:
    print("Division by zero not allowed")
    print("Modulo by zero not allowed")
    print(" Floor division by zero not allowed")  


print("\nAssignment Operations")
print(f"a = {a}\tb = {b}")
print("a will be assigned to x")
x = a
print("x=a is:", x)

x += b
print("x+=b is:", x)

x -= b
print("x-=b is:", x)

x *= b
print("x*=b is:", x)

if b != 0:
    x /= b  
else:
    x /= 1
print("x/=b is:", x)  

if b != 0:
    x %= b  
else:
    x %= 1
print("x%=b is:", x)

x **= 2
print("x**=2 is:", x) 
      
if b != 0:
    x //= b
else:
    x //= 1 
print("x//=b is:", x)


print("\nBitwise Operations")
print(f"{a} & {b} =", a & b)
print(f"{a} | {b} =", a | b)
print(f"{a} ^ {b} =", a ^ b)    
print(f"~{a} =", ~a)
print(f"{a} << 2 =", a << 2)
print(f"{a} >> 2 =", a >> 2)


print("\nComparison Operations")
print(f"{a} == {b} ", a == b)
print(f"{a} != {b} ", a != b)
print(f"{a} > {b} ", a > b)
print(f"{a} < {b} ", a < b) 
print(f"{a} >= {b} ", a >= b)
print(f"{a} <= {b} ", a <= b)


