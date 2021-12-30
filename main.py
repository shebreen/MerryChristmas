import turtle
import random

wn = turtle.Screen()
wn.setup(800, 600) 
wn.title("Christmas Tree")
wn.bgcolor("black")
board = turtle.Turtle()



widthText = turtle.numinput("Create christmas tree :","Width", default = 150)
heightText = turtle.numinput("Create christmas tree :","Height", default = 300)
board.speed(10)
for i in range(15):
    board.penup()
    board.goto(random.uniform(-300,300),random.uniform(-300,300))
    board.pendown()
    board.color('white')
    board.write('*', font=('arial',20,'bold'), align='center')


board.speed(3)
totalH = heightText
totalW = widthText

offsetY = totalH/3

upperTH = totalH*30/100
lowerTH = totalH*70/100
upperTW = totalW*30/100

triangleYOffset = upperTH/2

poleW = totalW*20/100
poleH = upperTH


board.color('green')
board.begin_fill()

board.penup()
board.goto(-1*upperTW/2,0 + offsetY)
board.pendown()

board.goto(upperTW/2,0 + offsetY)
board.goto(0,upperTH + offsetY)
board.goto(-1*upperTW/2,0 + offsetY)
board.end_fill()

board.begin_fill()
board.penup()
board.goto(0,triangleYOffset + offsetY)
board.pendown()

board.goto(-1*totalW/2,-1*(lowerTH+triangleYOffset) + offsetY)
board.goto(totalW/2,-1*(lowerTH+triangleYOffset) + offsetY)
board.goto(0,triangleYOffset + offsetY)


board.end_fill()

board.color('brown')
board.begin_fill()

board.penup()
board.goto(-1*poleW/2,-1*(lowerTH+triangleYOffset) + offsetY)
board.pendown()

board.goto(-1*poleW/2,-1*(lowerTH+triangleYOffset) + offsetY - poleH)
board.goto(poleW/2,-1*(lowerTH+triangleYOffset) + offsetY - poleH)
board.goto(poleW/2,-1*(lowerTH+triangleYOffset) + offsetY)
board.goto(-1*poleW/2,-1*(lowerTH+triangleYOffset) + offsetY)
board.end_fill()
board.penup()

board.color('red')
board.goto(0,totalH*2/3)
board.write('MERRY CHRISTMAS!', font=('arial',20,'bold'), align='center')

turtle.done()

