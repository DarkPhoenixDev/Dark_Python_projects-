from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.create_turtle()
    def create_turtle(self):
        self.shape("turtle")
        self.color("black")
        self.goto_start()
        self.setheading(90)
    def move_forward(self):
        new_y = self.ycor() + 10
        self.goto(x=0,y=new_y)
    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def goto_start(self):
        self.goto(STARTING_POSITION)
    
