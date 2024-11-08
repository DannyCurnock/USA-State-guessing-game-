import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S.A Game")
image = "days20-30/50States_USA/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("days20-30/50States_USA/50_states.csv")
state_list = data["state"].tolist()
guessed_states = []


# Use loop to keep user guessing 
# Keep tarck of the score 
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 states", prompt="Whats another state name?")
    answer_state = answer_state.strip().title()
    # Check if guess is among the 50 states 
    # Write correct guess onto map
    if answer_state == "Exit":
        not_guessed_states = [state for state in state_list if state not in guessed_states]
        df = pandas.DataFrame(not_guessed_states)
        df.to_csv("days20-30/50States_USA/not_guesses_states.csv")
        break
    if answer_state in state_list:
        print("correct")
        guessed_states.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == answer_state] # Pulls out row where the state is equal to the asnwer state
        new_turtle.goto(state_data.x.item(), state_data.y.item())
        new_turtle.write(answer_state)

# Figure out missiing states 


# Save missing states to csv file













