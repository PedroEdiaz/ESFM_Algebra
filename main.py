import parcial1 as p1
import parcial2 as p2

while True:
	print("""
Programa para Álgebra I-1
	1) Factorización en Primos
	2) MCD por Euclides
	3) Raices Cuadradas de complejos
	4) Raices Enesimas de complejos
Programa para Álgebra I-2
	5) Dividir de Polinomio
	6) Divición Sintética
	7) Maximo Común Divisor de Polinomio
	""")
	inp = int(input("> "))

	print('\n\section{Ejercicio}\n °')

	if (inp == 1):p1.fact()
	elif (inp == 2):p1.mcd()
	elif (inp == 3):p1.cuad()
	elif (inp == 4):p1.raices()
	elif (inp == 5):
		p2.fillPolin(f:=[]);
		p2.fillPolin(g:=[]); 
		p2.divPolin(f,g)
	elif (inp == 6):
		p2.fillPolin(f:=[])
		print("\nDividir por (ax+b):")
		g=[complex(input("a=\t")),complex(input("b=\t"))]
		p2.sintetica(f,g)
	elif (inp == 7):
		p2.fillPolin(f:=[]);
		p2.fillPolin(g:=[]); 
		p2.mcd(f,g)
	else: print("\nfuera de rango")
		

