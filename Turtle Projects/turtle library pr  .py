from turtle import Turtle,Screen
import time
# timmy = Turtle("turtle")
# print(timmy)

# timmy.shape("turtle")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

# def draw(no):
#     angle = 360/no
#     list = ["red",'blue','green','brown']
#     for i in range(no):
#         timmy.forward(100)
#         timmy.left(angle)
#         timmy.color(random.choice(list))
# for i in range(3,11):
#     draw(i)
# l = [0,90,180,270]
# timmy.speed(10)
# for i in range(200):
#     timmy.color(random.choice(list))
#     timmy.forward(100)
#     timmy.left(360)
# timmy.speed("fastest")
# def spirograph(size):
#     for i in range(int(360/size)):
#         list = ["red",'blue','green','brown']
#         timmy.color(random.choice(list))
#         timmy.circle(100)
#         current = timmy.heading()
#         timmy.setheading(current+size)
# spirograph(5)
  

# timmy.speed("fastest")
# list = ["red",'blue','green','brown','black']
# timmy.penup()
# timmy.hideturtle()
# timmy.setheading(255)
# timmy.forward(300)
# timmy.setheading(0)
# n = 100
# timmy.penup()
# for i in range(0,n+1):
#     timmy.dot(20,random.choice(list))
#     timmy.forward(50)
#     if i % 10 == 0:
#         timmy.setheading(90)
#         timmy.forward(50)
#         timmy.setheading(180)
#         timmy.forward(500)
#         timmy.setheading(0)


# timmy.shape("turtle")
# def forward():
#     timmy.forward(10)
# def backword():
#     timmy.back(10)
# def left():
#     timmy.left(90)
# def right():
#     timmy.right(90)
# def clear ():
#     timmy.penup()
#     timmy.clear()
#     timmy.home()
#     timmy.pendown()
# myscreen = Screen()
#  myscreen.listen()
# myscreen.onkey(key = "w", fun = forward)
# myscreen.onkey(key = "s", fun = backword)
# myscreen.onkey(key = "a", fun = left)
# myscreen.onkey(key = "d", fun = right)
# myscreen.onkey(clear,"c")
# ison = False
# myscreen = Screen()
# myscreen.setup(width = 500,height = 400)
# user = myscreen.textinput(title = "make your bet", prompt = "whic turtle gonna win the race ")
# color = [ "black","red","blue","green","yellow","orange"]
# allturtle = []
# y_cordinte = [-70 ,-40 ,-10 ,20,50,80 ]
# for i in range(0,6):
#     new_turtle = Turtle("turtle")
#     new_turtle.color(color[i])
#     new_turtle.penup()
#     new_turtle.goto(x =-230,y = y_cordinte[i] )
#     allturtle.append(new_turtle)
# if user:
#     ison = True
# while ison:
#     for turtle in allturtle:
#          random_number = random.randint(0,10)
#          turtle.forward(random_number)
#          if turtle.xcor() > 230:
#             ison = False
#             winner = turtle.pencolor()
#             if winner == user:
#                 print(f"you won the bet {winner} win the race")
#             else:
#                 print(f"you lost the {winner} won the race")

