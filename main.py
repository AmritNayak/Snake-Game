from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=700)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()

    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        scoreboard.reset()
        snake.reset()

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    screen.update()

screen.exitonclick()
