def add(a, b):
    return a + b

def subtract(a, b):
    return a+b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b!=0:
        return a/b
    else:
        print("division by zero not allowed")
        
while True:
    print("\nMenu:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiply")
    print("4. divide")
    print("5. Exit")
    
    choice=int(input("enter one of above items"))
    if choice==5:
        print("exit program.")
        break
    num1=float(input("enter the first number"))
    num2=float(input("Enter the second number"))

    if choice==1:
        print("Result: ", add(num1 , num2))
    elif choice==2:
        print("Result: ", subtract(num1 , num2))
    elif choice==3:
        print("Result: ", multiply(num1 , num2))
    elif choice==4:
        print("Result: ", divide(num1 , num2))
    else:
        print("invalid choice pleaze enter the correct choice")
    