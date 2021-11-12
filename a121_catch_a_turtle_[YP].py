# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_size = 2
score = 0
font_setup = ("Arial", 20, "normal")
colors = ["black", "sky blue", "salmon", "orchid", "pale green"]

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name: ")

#-----initialize turtle-----
spot = trtl.Turtle()


#-----game functions--------
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-250,250)

def spot_clicked(x,y):
  counter.getscreen()
  if(timer!=0):
    update_score()
    change_position()

  else:
    spot.hideturtle()
  
# resize the turtle
def resize():
  sizes = [.5, 1, 1.5, 2]
  spot.shapesize(rand.choice(sizes))

# stamp turtle
def leave_a_mark():
  spot.fillcolor(rand.choice(colors[1:]))
  spot.stamp()
  spot.fillcolor(colors[0]) # comment out for more a more difficult game

def change_position():
  leave_a_mark()
  resize() 
  new_xpos = rand.randint(-150, 150) 
  new_ypos = rand.randint(-150, 150) 
  spot.penup() 
  spot.hideturtle() 
  spot.goto(new_xpos,new_ypos) 
  spot.showturtle()

def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)


#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(200, -200)

#-----game functions-----
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 



# starting the game
def start_game():
  spot.onclick(spot_clicked)
  counter.getscreen().ontimer(countdown, counter_interval)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global t 

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

#-----events----------------
start_game()
wn = trtl.Screen()
wn.bgcolor("sky blue")
wn.mainloop()
