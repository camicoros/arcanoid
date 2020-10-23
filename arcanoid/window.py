from tkinter import *
import time

from ball import Ball
from paddle import Paddle
from score import Score

tk = Tk()
tk.title('Aracanoid v1.0')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()
tk.update()

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'White')
balls = []
ball = Ball(canvas, paddle, score, 'red')
balls.append(ball)


def ball_destroyer(canvas, balls_list):
    if isinstance(balls_list, list):
        for ball in balls_list:
            if isinstance(ball, Ball):
                if ball.hit_bottom:
                    balls_list.remove(ball)
                    canvas.delete(ball.id)


while len(balls) > 0:
    if paddle.started:
        ball_destroyer(canvas, balls)
        for ball in balls:
            ball.draw()
            if ball.hit_paddle(canvas.coords(ball.id)):
                balls.append(Ball(canvas, paddle, score, 'red'))
        paddle.draw()
    if len(balls) == 0:
        canvas.create_text(250, 120, text='ты хуй', font=('Courier', 110), fill='red')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
time.sleep(3)