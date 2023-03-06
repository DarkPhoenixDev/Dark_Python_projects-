from turtle import Turtle
class Pabble(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_pabble()
    def create_pabble(self):
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x=350,y=0)
    def up (self):
        self.new_y = self.ycor() + 20
        self.goto(x=self.xcor(),y=self.new_y)
    def down (self):
        self.new_y = self.ycor() - 20
        self.goto(x=self.xcor(),y=self.new_y)




class Pabble2(Pabble):
    def __init__(self) -> None:
        super().__init__()
    def create_pabble2(self):
        self.goto(x=-350,y=0)


    

