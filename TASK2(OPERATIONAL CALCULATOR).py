def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Error! Division by Zero."
def calculator():
    num1=float(input("Enter the first Number:"))
    num2=float(input("Enter the second Number"))
    print("Choose an operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=input("Enter choice(1 to 4):")
    if choice == '1':
        print("Results:",add(num1,num2))
    elif choice=='2':
        print("Result:",subtract(num1,num2))
    elif choice == '3':
        print("Result:",multiplication(num1,num2))
    elif choice =='4':
        print("Result:",divide(num1,num2))
    else:
        print("Invalid Input")
calculator()