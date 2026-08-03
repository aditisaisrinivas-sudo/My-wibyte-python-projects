
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

x_val = -350
y_val = 0


for kk in range(35):
        if kk < 5:
            draw_rectangle(x_val, y_val, 20, 20, "red")

        elif 5<=kk<10:
            draw_rectangle(x_val, y_val, 20, 20, "blue")
        elif 10<=kk<15:
            draw_rectangle(x_val, y_val, 20, 20, "orange")
        elif 15<=kk<20:
            draw_rectangle(x_val, y_val, 20, 20, "gold")
        elif 20<=kk<25:
            draw_rectangle(x_val, y_val, 20, 20, "orange")
        elif 25<=kk<30:
            draw_rectangle(x_val, y_val, 20, 20, "blue")
        else:
            draw_rectangle(x_val, y_val, 20, 20, "red")

        x_val = x_val + 20

#add another row (up 20)
x_val = -350
y_val = y_val + 20

for kk in range(35):
        if kk % 2 !=0:
            draw_rectangle(x_val, y_val, 20, 20, "purple")

        else:
            draw_rectangle(x_val, y_val, 20, 20, "pink")

        x_val = x_val + 20

x_val = -350
y_val = y_val -40

for kk in range(35):
        if kk % 2 !=0:
            draw_rectangle(x_val, y_val, 20, 20, "purple")

        else:
            draw_rectangle(x_val, y_val, 20, 20, "pink")

        x_val = x_val + 20

x_val = -350
y_val = y_val +60

for kk in range(35):
        if kk < 5:
            draw_rectangle(x_val, y_val, 20, 20, "red")
        elif 5<=kk<10:
            draw_rectangle(x_val, y_val, 20, 20, "blue")
        elif 10<=kk<15:
            draw_rectangle(x_val, y_val, 20, 20, "orange")
        elif 15<=kk<20:
            draw_rectangle(x_val, y_val, 20, 20, "goldn")
        elif 20<=kk<25:
            draw_rectangle(x_val, y_val, 20, 20, "orange")
        elif 25<=kk<30:
            draw_rectangle(x_val, y_val, 20, 20, "blue")
        else:
            draw_rectangle(x_val, y_val, 20, 20, "red")

        x_val = x_val + 20


x_val = -350
y_val = y_val - 80

for kk in range(35):
        if kk < 5:
            draw_rectangle(x_val, y_val, 20, 20, "red")
        elif 5<=kk<10:
            draw_rectangle(x_val, y_val, 20, 20, "blue")
        elif 10<=kk<15:
            draw_rectangle(x_val, y_val, 20, 20, "orange")
        elif 15<=kk<20:
            draw_rectangle(x_val, y_val, 20, 20, "gold")
        elif 20<=kk<25:
            draw_rectangle(x_val, y_val, 20, 20, "orange")
        elif 25<=kk<30:
            draw_rectangle(x_val, y_val, 20, 20, "blue")
        else:
            draw_rectangle(x_val, y_val, 20, 20, "red")

        x_val = x_val + 20
    



turtle.mainloop()

