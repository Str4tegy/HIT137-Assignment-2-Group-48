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
        try:
            sides = int(input("Enter the number of sides "))
            if int (sides) < 0:
                sides=print("Please enter a positive integer")
                continue
            else:
                break
        except ValueError:
                sides=print("Please enter a positive integer")

    while True:
        try:
            length = float(input("Enter the side length "))
            if float (length) < 0:
                length=print("Please enter a positive number")
                continue
            else:
                break
        except ValueError:
                length=print("Please enter a positive number")

    while True:
        try:
            depth = int(input("Enter the recursion depth "))
            if int (depth) < 0:
                depth=print("Please enter a positive integer")
                continue
            else:
                break
        except ValueError:
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
