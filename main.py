import turtle
import time
import random

delay=0.1
score=0
high_score=0
#set window
window=turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600,height=600)
window.tracer(0)  #turn off all the updates

#create a snake 
head=turtle.Turtle()
head.color("black")
head.shape("square")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction="stop" #unclear

#create food
food=turtle.Turtle()
food.color("red")
food.shape("circle")
food.speed(0)
food.penup()
food.goto(0,100)

segments = []


#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0    High Score : 0 ",font=("times new roman",24,"normal"),align="center")
#set direction
def go_up():
    if head.direction !="down":
        head.direction = "up"

def go_down():
    if head.direction !="up":
        head.direction = "down"

def go_left():
    if head.direction !="right":
        head.direction = "left"

def go_right():
    if head.direction !="left":
        head.direction = "right"


#move head
def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y+20)

    elif head.direction == "down":
        y=head.ycor()
        head.sety(y-20)    

    elif head.direction == "left":
        x=head.xcor()
        head.setx(x -20)    

    elif head.direction == "right":
        x=head.xcor()
        head.setx(x + 20)    

#keyboard binding
turtle.listen()
turtle.onkeypress(go_up,"Up")
turtle.onkeypress(go_down,"Down")
turtle.onkeypress(go_left,"Left")
turtle.onkeypress(go_right,"Right")        
while True:
    window.update() #update the screen

    #check for collision with border
    if head.xcor() <-290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() >290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

        #reset score
        score = 0
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score,high_score),align="center",font=("times new roman",24,"normal"))


    #check for collision with food
    if head.distance(food) < 20:
        #place food at random position
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("grey")
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)

        #shorten delay
        delay -=0.001
        #increase score
        score +=10

        if score > high_score:
            high_score=score

        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score,high_score),align="center",font=("times new roman",24,"normal"))
        
    #previous block is moving to its succesor's x and y    
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        
    #move segment 0 to where the head is 
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    
    move()

    #check for head collision with body segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score : {}  High Score : {}".format(score,high_score),align="center",font=("times new roman",24,"normal"))



    time.sleep(delay)
window.mainloop()