import turtle

n=int(input("Enter the number of iterations = "))

t=turtle.Turtle()
sc=turtle.Screen()

sc.bgcolor("black")

for i in range(n):
    
    if((i+1)%2==0):
        t.color("cyan")
    else:
        t.color("blue")    
    
    t.left(23)

    for j in range(4):
        t.forward(150)
        t.left(90)