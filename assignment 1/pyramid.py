def printtraingle(height):
    for i in range(1,height+1):
        print(" " * (height - i), end="")   # This print spaces
        print("*" * (2 * i - 1))    # This print *
height = int(input("Enter the height of the triangle : "))

printtraingle(height)