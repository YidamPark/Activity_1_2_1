# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_size = 2
score = 0
font_setup = ("Arial", 20, "normal")

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
  

def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-200,200)
  spot.penup()
  spot.hideturtle()
  spot.goto(new_xpos,new_ypos)
  spot.pendown()
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
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.bgcolor("sky blue")
wn.mainloop()