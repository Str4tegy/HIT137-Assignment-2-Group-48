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
    sides = int(input("Enter the number of sides: "))
    length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    turtle.speed(0)  
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-length/2, length/2)  
    turtle.pendown()

    DrawPolygon(sides, length, depth)

    turtle.done()

if __name__ == "__main__":
    main()
