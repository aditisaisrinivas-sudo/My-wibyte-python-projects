
import turtle
t = turtle.Turtle()

def draw_line(x0,y0,x1,y1):
    t.penup()
    t.goto(x0,y0)
    t.pendown()
    t.goto(x1,y1)


def draw_rectangle(x0,y0,len,hgt,clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0,y0,x0+len,y0)
    draw_line(x0+len,y0,x0+len,y0+hgt)
    draw_line(x0+len,y0+hgt,x0,y0+hgt)
    draw_line(x0,y0+len,x0,y0)
    t.end_fill()

x_val = -200
y_val = 0


for kk in range(20):
        if kk < 5:
            draw_rectangle(x_val, y_val, 20, 20, "red")

        else:
            draw_rectangle(x_val, y_val, 20, 20, "green")

        x_val = x_val + 20




turtle.mainloop()

