import turtle                                                   #Required for turtle graphics

i=0                                                             #Defining the variable required for later loops

def DrawEdge(length, depth):
    if depth == 0:                                              #Base case - Draw a straight line if the recursion depth is equal to 0
        turtle.forward(length)
    else:
         length /= 3.0                                          #Otherwise, split the line into 3 equal parts
         for i in range (0,3):                                  #Create a loop which repeats 3 times
              DrawEdge(length, depth -1)                        #Draw one segment
              turtle.right((60+180*i))                          #Change the direction of the turtle so the 3 segments form a triangle
              i+=1                                              #Necessary for the loop
         DrawEdge(length, depth -1)                             #Drawing the fourth segment

def DrawPolygon(sides, length, depth):
    for _ in range(sides):
        DrawEdge(length, depth)                                 #Drawing one fractal edge
        turtle.right(360 / sides)                               #Rotate direction for next side

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

    turtle.speed(0)                                             #These are the turtle configuration settings
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-length/2, length/2)  
    turtle.pendown()

    DrawPolygon(sides, length, depth)                           #Drawing the fractal polygon

    turtle.done()                                               #Keeps window open until user closes it

if __name__ == "__main__":
    main()
