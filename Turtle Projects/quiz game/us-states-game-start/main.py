import turtle
import pandas
screen = turtle.Screen()
screen.title("Us Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)  


data1 = pandas.read_csv("50_states.csv")
data = data1.state.to_list()
guessed_state = []

while len(guessed_state)<50:
      answer = screen.textinput(title=f"guess the state {len(guessed_state)}/50",
                                prompt="whats the state name").title()
      if answer == "Exit":
          missing_states=[state for state in data if state not in guessed_state]
          new_data = pandas.DataFrame(missing_states)
          new_data.to_csv("states_to_learn")
          break      
      if answer in data:
         guessed_state.append(answer)
         t=turtle.Turtle()
         t.hideturtle()
         t.penup()
         state = data1[data1.state==answer] 
         t.goto(int(state.x),int(state.y))
         t.write(state.state)
     
screen.exitonclick()