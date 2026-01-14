a=float(input("Enter number1 : "))
b=float(input("Enter number2 : "))
op = input("Enter + - * / : ")
if op =="+" :
    print(f"sum = {a+b}")
elif op == "-" :
    print(f"Difference = {a-b}")
elif op == "*" :        
    print(f"Product= {a*b}")
elif op == "/" :
    print(f"Quotient = {a/b}")
else:
    print("Invalid Operator")
    