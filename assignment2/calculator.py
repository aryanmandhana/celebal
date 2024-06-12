def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print("---**---**---Select the operation you want to do---**---**--- \n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice : "))
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
if choice == 1:
    print("The sum of the two numbers is : ",add(num1,num2))
elif choice == 2:
    print("The difference of the two numbers is : ",sub(num1,num2))
elif choice == 3:
    print("The product of the two numbers is : ",mul(num1,num2))
elif choice == 4:
    print("The division of the two numbers is : ",div(num1,num2))
else:
    print("Invalid choice")

    