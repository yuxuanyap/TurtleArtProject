
#exploring colrmode and loop variable
import turtle
turtle.colormode(255)

bob=turtle.Turtle()
bob.width(2)
bob.speed(11)
turtle.bgcolor(0,0,0)
turtle.colormode(255)#adds the colormode function
c=(46,139,87) #c is the variable to store values of r,g,b
c=(46,139,87)


for times in range(256):
    c=(0,255,times) #loop variable is the value of c
    bob.color(c) #c is the variable
    bob.forward(times*3+3)
    bob.right(165)
    bob.forward(100)
    bob.right(1)
   
    
for times in range(90):
    for c in ["purple", "red","blue", "green"]:
        bob.begin_fill()
        bob.goto(-50,0)
        bob.color(c) #c is the variable
        bob.forward(times*2+2)
        bob.right(80)
        bob.forward(10)
        bob.right(80)
        bob.right(1)
        bob.end_fill()

for times in range(80):
    c=(255,255,0) #loop variable is the value of c
    bob.color(c) #c is the variable
    bob.begin_fill()
    bob.goto(-50,0)
    bob.color(c) #c is the variable
    bob.forward(times*2+2)
    bob.right(150)
    bob.forward(10)
   


for times in range(80):
    c=(times,0,times) #loop variable is the value of c
    bob.color(c) #c is the variable
    bob.begin_fill()
    bob.goto(-50,0)
    bob.color(c) #c is the variable
    bob.forward(times*1+1)
    bob.right(175)
    bob.forward(10)





   





        
   
