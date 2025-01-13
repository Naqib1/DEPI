def Calcuture():
    while(True):
        operation=input("Choose an operation: ")
        num_1=float(input("Enter first number: "))
        num_2=float(input("Enter second number: "))
        if operation in ('+'):
            print("Result:",(num_1+num_2))
        elif operation in ('-'):
            print("Result:",(num_1-num_2))
        elif operation in ('*'):
            print("Result:",(num_1*num_2))
        elif operation in ('/'):
            if num_2!=0:
                print("Result:",(num_1/num_2))
            else:
                print("Error: Division by zero is not allowed")
        again=input("Would you like to deal with him again?\nYes or No: " )
        if again.lower() != "yes":
            break
Calcuture()