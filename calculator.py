print("====Python Calculator====")
print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit")
a=int(input("Enter your Choice:")) 
if a==1:
    b=int(input("Enter first number:"))
    c=int(input("Enter second number:"))
    print(b,"+",c,"=",b+c)
elif a==2:
    b=int(input("Enter first number:"))
    c=int(input("Enter second number:"))
    print(b,"-",c,"=",b-c)
elif a==3:
    b=int(input("Enter first number:"))
    c=int(input("Enter second number:"))
    print(b,"*",c,"=",b*c)  
elif a==4:
    b=int(input("Enter first number:"))
    c=int(input("Enter second number:"))
    if c==0:
        print("Error! Division by zero.")
    else:
        print(b,"/",c,"=",b/c)
elif a==5:
    print("Exiting the calculator. Goodbye!")   
else:
    print("Invalid input! Please enter a valid choice.")    
print("Thank you for using the calculator.")                            