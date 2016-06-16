a=int(input("INGRESE UN NUMERO: "))
import turtle 
t=turtle.Pen()

if(a==0 or a==1 or a==2):
	print("NO SE PUEDE DIBUJAR UNA FIGURA CON ESE NUMERO DE LADOS")

for x in range(0,a):
	t.forward(-30)
	t.left(360/a)
turtle.getscreen()._root.mainloop()
