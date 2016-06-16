import turtle 
t=turtle.Pen()

t.forward(-200)
t.left(10)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)

t.reset()
for x in range(1,9):
	t.forward(100)
	t.left(225)
turtle.getscreen()._root.mainloop()