import random


BALL_COLORS = ('green', 'yellow', 'red', 'blue', 'orange', 'violet')


class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=random.choice(BALL_COLORS))
        self.canvas.move(self.id, 245, 100)
        starts = [x for x in (list(range(-10, -1))+list(range(1, 10)))]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                self.score.hit()
                self.canvas.itemconfig(self.id, fill=random.choice(BALL_COLORS))
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            # self.canvas.create_text(250, 120, text='ты хуй', font=('Courier', 110), fill='red')
        if self.hit_paddle(pos):
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2
