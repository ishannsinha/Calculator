while(True):
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y
    def multiply(x,y):
        return x*y
    def divide(x,y):
        return x/y
    print("====Python Calculator====")    
    print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit")   
    a=int(input("Enter your Choice:")) 
    if(1<=a<=4):
        x=int(input("Enter first number:"))
        y=int(input("Enter second number:"))
        if(a==1):
            print("Addition of two numbers is:",add(x,y))
        elif(a==2):
            print("Subtraction of two numbers is:",subtract(x,y))
        elif(a==3):
            print("Multiplication of two numbers is:",multiply(x,y))
        elif(a==4):
            print("Division of two numbers is:",divide(x,y))    
    elif(a==5):
        print("Exiting the calculator...")
        break
    else:
        print("Invalid choice. Please try again.")
    print("Thank you for using the calculator!")            
    
    