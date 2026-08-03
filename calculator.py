print("====Python Calculator====")
print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit")
a=int(input("Enter your Choice:"))
while a!=5:
    if a==1:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print(num1,"+",num2,"=",num1+num2)
        break
    elif a==2:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print(num1,"-",num2,"=",num1-num2)
        break    
    elif a==3:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print(num1,"*",num2,"=",num1*num2)
        break
    elif a==4:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if num2==0:
            print("Error! Division by zero.")
        else:
            print(num1,"/",num2,"=",num1/num2)
        break        
    else:
        print("Invalid Input")
        break
print("Exiting the calculator. Goodbye!")        
