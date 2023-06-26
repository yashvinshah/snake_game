from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # FOOD COLLISION
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.inc_score()

    # DETECT WALL COLLISION
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # DETECT TAIL COLLISION
    for x in snake.segments[1:]:
        if snake.head.distance(x) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
