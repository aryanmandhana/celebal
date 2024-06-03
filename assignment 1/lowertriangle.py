def printtraingle(height):
    for i in range(height, 0, -1):
        print('*' * i)
height = int(input("Enter the height of the triangle : "))

printtraingle(height)