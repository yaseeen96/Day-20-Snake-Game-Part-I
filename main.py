from turtle import Screen, Turtle
from snake import Snake
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="a", fun=snake.left)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
     



screen.exitonclick()