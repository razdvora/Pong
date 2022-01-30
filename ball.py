from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce(self,x,y):
        self.y_move *= y
        self.x_move *= x

    def reset_position(self):
        self.goto(0, 0)
        self.bounce(-1, 1)