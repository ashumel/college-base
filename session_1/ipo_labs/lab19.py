import turtle

tl = turtle.Turtle()
tl.speed(0)
tl.pensize(4)

def pixel():
    for x in range(4):
        tl.forward(20)
        tl.right(90)


def draw_pixels(count : int, color = 'Black'):
    tl.begin_fill()
    tl.color(color)
    for x in range(count):
        pixel()
        tl.forward(20)
    tl.end_fill()


def set_xy(count):
    tl.sety(tl.ycor() - 20)
    tl.setx(tl.xcor() - 20 * count)


def repeat_center():
    draw_pixels(1)
    draw_pixels(2, 'White')
    draw_pixels(1)
    draw_pixels(6, 'Orange')
    draw_pixels(1)
    draw_pixels(3, 'White')
    draw_pixels(1)


def repeat_line_1():
    draw_pixels(2)
    draw_pixels(5, 'White')
    draw_pixels(2)


def repeat_line_2():
    draw_pixels(1)
    draw_pixels(9, 'White')
    draw_pixels(1)


def repeat_line_3():
    draw_pixels(1)
    draw_pixels(3, 'White')
    draw_pixels(4)
    draw_pixels(4, 'White')
    draw_pixels(1)


draw_pixels(5)
set_xy(7)
repeat_line_1()
set_xy(10)
repeat_line_2()
set_xy(12)
repeat_line_3()
set_xy(13)
draw_pixels(1)
draw_pixels(2, 'White')
draw_pixels(1)
draw_pixels(4, 'Orange')
draw_pixels(1)
draw_pixels(3, 'White')
draw_pixels(1)
set_xy(14)
draw_pixels(1)
draw_pixels(2, 'White')
draw_pixels(1)
draw_pixels(1, 'Orange')
draw_pixels(1, 'White')
draw_pixels(4, 'Orange')
draw_pixels(1)
draw_pixels(3, 'White')
draw_pixels(1)
set_xy(15)
repeat_center()
set_xy(15)
repeat_center()
set_xy(15)
repeat_center()
set_xy(15)
draw_pixels(1)
draw_pixels(3, 'White')
draw_pixels(1)
draw_pixels(4, 'Orange')
draw_pixels(1)
draw_pixels(4, 'White')
draw_pixels(1)
set_xy(14)
repeat_line_3()
set_xy(13)
draw_pixels(1)
draw_pixels(11, 'White')
draw_pixels(1)
set_xy(12)
repeat_line_2()
set_xy(10)
repeat_line_1()
set_xy(7)
draw_pixels(5)

turtle.mainloop()