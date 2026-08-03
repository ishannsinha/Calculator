print("====Python Calculator====")
print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit")
a=int(input("Enter your Choice:"))
b=int(input("Enter first number:"))
c=int(input("Enter second number:"))
if a==1:
    print("Addition of two numbers is:",b+c)
elif a==2:
    print("Subtraction of two numbers is:",b-c)
elif a==3:
    print("Multiplication of two numbers is:",b*c)
elif a==4:
    print("Division of two numbers is:",b/c)
elif a==5:
    print("Exiting...")
else:
    print("Invalid Choice")
print("Thank you for using the calculator!")    