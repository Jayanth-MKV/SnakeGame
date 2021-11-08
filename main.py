from turtle import Screen, down, left
from snake import Snake
import time
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Hungry Snake")
screen.tracer(0)

snake = Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




gamepos=True
while gamepos:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.incre()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        gamepos=False
        score.gameover()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            gamepos=False
            score.gameover()    

screen.exitonclick()