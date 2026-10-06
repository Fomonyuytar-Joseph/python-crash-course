import turtle as turtle_module
import random

tim = turtle_module.Turtle()

turtle_module.colormode(255)
tim.penup()
tim.hideturtle()



color_list = [(251, 249, 245), (205, 164, 126), (248, 229, 234), (231, 245, 235), (164, 168, 36), (244, 78, 55), (142, 49, 105), (216, 230, 234), (239, 66, 135), (6, 142, 56), (237, 110, 164), (3, 142, 185), (52, 201, 225), (161, 55, 51), (245, 223, 49), (20, 166, 126), (252, 230, 0), (117, 36, 86), (27, 192, 212), (115, 188, 152), (237, 165, 193), (238, 170, 155), (3, 113, 26), (136, 215, 227), (150, 214, 183), (137, 36, 32), (82, 29, 76), (102, 14, 12)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1 , num_of_dots + 1):
     tim.dot(20,random.choice(color_list))
     tim.forward(50)

     if dot_count % 10 == 0:
          tim.setheading(90)
          tim.forward(50)
          tim.setheading(180)
          tim.forward(500)
          tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()


# # Extract 6 colors from an image.

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# print(colors)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
