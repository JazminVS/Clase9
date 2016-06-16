#EJERCICIO 7
lados=int(input("INGRESE EL NUMERO DE LADOS: "))
tam=int(input("INGRESE EL TAMAÑO: "))

import turtle
t= turtle.Pen()

def poligono ():
	for x in range(0,lados):
		t.forward(tam)
		t.left(360/lados)
poligono()

turtle.getscreen()._root.mainloop()


