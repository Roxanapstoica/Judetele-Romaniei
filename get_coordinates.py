from turtle import Turtle, Screen


def get_mouse_click_coor(x, y):
    print(x, y)


BACKGROUND = "romania_map_blank.gif"
screen = Screen()
state_to_be_written = Turtle()
background_map = Turtle()
screen.title("Judetele Romaniei")
screen.addshape(BACKGROUND)
background_map.shape(BACKGROUND)

t = Turtle()

screen.onscreenclick(get_mouse_click_coor)

screen.mainloop()
#screen.exitonclick()
