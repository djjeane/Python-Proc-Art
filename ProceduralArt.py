import tkinter as tk
import turtle
from PIL import ImageGrab
# fibonacci sequence generator


def dump_gui(root):
    """
    takes a png screenshot of a tkinter window, and saves it on in cwd
    """
    print('...dumping gui window to png')

    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    w = x0 + root.winfo_width()
    h = y0 + root.winfo_height()
    ImageGrab.grab(bbox=(x0, y0, w, h)).save("imgs\gui_image_grabbed.png")


def fib(n, t):
    turtle.tracer(0, 0)

    if n <= 1:
        return 0
    else:
        SQUARES = n
        SIDE = n
        shade = 1.0
        for count in range(SQUARES):
            t.fillcolor(shade, shade, shade)
            t.begin_fill()
            t.left(360 // SQUARES)
            for side in range(4):
                t.forward(SIDE)
                t.left(90)
            t.end_fill()
            shade -= turtle.colormode() / float(SQUARES)

        turtle.update()
        return fib(n - 1, t) + fib(n - 2, t)


def draw(t):
    for n in range(10):
        for i in range(10):
            t.forward(i+3)
            t.right(90)
        t.right(45)
    turtle.update()


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    t = turtle.RawTurtle(canvas)
    t.speed(0)
    t.hideturtle()
    turtle.tracer(0, 0)

    # start = 100
    # fib(start, t)
    draw(t)
    dump_gui(canvas)


if __name__ == '__main__':
    main()
