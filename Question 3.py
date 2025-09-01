import turtle

def DrawEdge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        DrawEdge(length, depth - 1)
        turtle.right(60)
        DrawEdge(length, depth - 1)
        turtle.left(120)
        DrawEdge(length, depth - 1)
        turtle.right(60)
        DrawEdge(length, depth - 1)

def DrawPolygon(sides, length, depth):
    for _ in range(sides):
        DrawEdge(length, depth)
        turtle.right(360 / sides)

def main():
    while True:
        try:                                                    #Recieves an integer input from the user regarding the number of sides.
            sides = int(input("Enter the number of sides "))    
            if int (sides) < 0:                                 #Checks that the input is positive, and if it is negative, it tells the user to enter a positive integer and repeats the loop of asking for an integer input.
                sides=print("Please enter a positive integer")  
                continue
            else:                                               #If the input is not a ValueError or negative, it breaks the loop and accepts the input.
                break
        except ValueError:                                      #If there is a ValueError, it asks the user for an positive integer and repeats the loop of asking for an integer input.
                sides=print("Please enter a positive integer")

    while True:
        try:                                                    #Recieves a float input from the user regarding the lenght of each side.
            length = float(input("Enter the side length "))     
            if float (length) < 0:                              #Checks that the input is positive, and if it is negative, it tells the user to enter a positive number, and repeats the loop of asking for a float input.
                length=print("Please enter a positive number")
                continue
            else:                                               #If the input is not a ValueError or negative, it breaks the loop and accepts the input.
                break
        except ValueError:                                      #If there is a ValueError, it asks the user for a positive number and repeats the loop of asking for a float input.
                length=print("Please enter a positive number")

    while True:
        try:                                                    #Recieves an integer input from the user regarding the recursion depth.
            depth = int(input("Enter the recursion depth "))
            if int (depth) < 0:                                 #Checks that the input is positive, and if it is negative, it tells the user to enter a positive integer, and repeats the loop of asking for an integer input.
                depth=print("Please enter a positive integer")
                continue
            else:                                               #If the input is not a ValueError or negative, it breaks the loop and accepts the input.
                break
        except ValueError:                                      #If there is a ValueError, it asks the user for a positive integer and repeats the loop of asking for an integer input. 
                depth=print("Please enter a positive integer")

    turtle.speed(0)  
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-length/2, length/2)  
    turtle.pendown()

    DrawPolygon(sides, length, depth)

    turtle.done()

if __name__ == "__main__":
    main()
