from turtle import Turtle
UP=90
DOWN=270
RIGHT=0
LEFT=180

DIST=20
STARTING_POS=[(0,0),(-20,0),(-40,0)]

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments=[]
        self.makesnake()
        self.head=self.segments[0]
    
    def makesnake(self):
        for pos in STARTING_POS:
            self.addseg(pos)
           
    def addseg(self,pos):
        newseg=Turtle("square")
        newseg.color("white")
        newseg.penup()
        newseg.goto(pos)
        self.segments.append(newseg)


    def extend(self):
        self.addseg(self.segments[-1].position())

    def move(self):
        for num in range(len(self.segments)-1,0,-1):
            newx=self.segments[num-1].xcor()
            newy=self.segments[num-1].ycor()
            self.segments[num].goto(newx,newy)
        self.head.forward(DIST)


    def up(self):
        if self.head.heading()!=DOWN :
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading()!=UP :
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading()!=RIGHT :
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT :
            self.head.setheading(RIGHT)

