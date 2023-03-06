from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x= 0,y=270)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"score : {self.score} High score : {self.highscore}",align= "center",font = ("arial",24,"normal"))
    def gameover (self):
        self.goto(0,0)
        self.write("GAME OVER", align= "center",font = ("arial",24,"normal"))
    def increase(self):
        self.score+=1
        self.update_score()
    def refresh_score(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("data.txt","w") as data:
                 data.write(f"{self.highscore}")
            self.score = 0
        self.update_score()
    
    

       
