'''Write a Python program that:
Takes two integer inputs from the user.
Asks the user to choose a calculation type: Add, Subtract, Multiply, or Divide (case-insensitive).
Performs the selected calculation and displays the result.
Handles division by zero by printing an error message.
Handles invalid number inputs by displaying an appropriate error message.
Displays an error message if the user selects an invalid operation.'''
#**************************************************************************************************************

#use exception handling (try-except) to catch invalid inputs (e.g., if the user enters text instead of a number).
try:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second nummer:"))

    print("Choose Calculations to Perform:\n",
    "1. Add\n"
    "2. Subtract\n"
    "3. Multiply\n"
    "4. Divide")

    cal=input().strip().lower()

    if cal=="add":
        ans=num1+num2
    elif cal=="subtract":
        ans=num1-num2
    elif cal=="multiply":
        ans= num1*num2
    elif cal=="divide":
        if num2==0:
            print("Error! Can't divide by zero.")
            ans=None
        else:
            ans=num1/num2
    else: 
        print("Invalid OPeration!")
        ans=None

    if ans is not None:
        print(f"The Answer is : {ans}")  
except ValueError:
    print("Ivalid Input! Please Enter valid number!")
