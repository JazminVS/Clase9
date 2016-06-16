a=int(input("INGRESE EL TAMAÑO "))
import turtle
t= turtle.Pen()

for x in range (1,5):
	t.forward(a)
	t.left(90)


turtle.getscreen()._root.mainloop()