while(True):
    print("====Python Calculator====")
    print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit")
    a=int(input("Enter your Choice:")) 
    if(1<=a<=4):
        if(0<a<5):
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
            if(a==1):
                print(num1,"+",num2,"=",num1+num2)
            elif(a==2):
                print(num1,"-",num2,"=",num1-num2)
            elif(a==3):
                print(num1,"*",num2,"=",num1*num2)
            elif(a==4):
                if(num2!=0):
                    print(num1,"/",num2,"=",num1/num2)
                else:
                    print("Error! Division by zero.")
    else:
        print("Exiting the calculator. Goodbye!")
        break
print("Thank you for using the calculator. Goodbye!")