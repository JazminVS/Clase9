import time
from tkinter import *
tk=Tk()

canvas=Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

for x in range (0,90):
	canvas.move(1,5,0)
	tk.update()
	time.sleep(0.05)

tk.mainloop()


