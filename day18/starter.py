from turtle import Turtle , Screen
import random

tim = Turtle()

colors = ["red", "blue", "green", "orange", "purple",
          "yellow", "pink", "brown", "cyan", "magenta"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
      tim.forward(200)
      tim.right(angle)


for shape_side_n in range(3, 11):
   tim.color(random.choice(colors))
   draw_shape(shape_side_n)




# num_of_sides = 3


# while num_of_sides < 11:
  
#   angle = 360 / num_of_sides
#   for _ in range(num_of_sides):
#      tim.forward(200)
#      tim.right(angle)
  
#   num_of_sides+=1




# for _ in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

# tim.forward(10)
# tim.penup()
# tim.forward(10)
# tim.pendown()










# tim.shape("turtle")
# tim.color("red")

# for _ in range(4):
#    tim.forward(200)
#    tim.left(90)



# tim.forward(200)
# tim.left(90)
# tim.forward(200)
# tim.left(90)
# tim.forward(200)
# tim.left(90)




# tim.forward(200)
# tim.left(-90)
# tim.forward(200)
# tim.right(90)
# tim.forward(200)


screen = Screen()

screen.exitonclick()