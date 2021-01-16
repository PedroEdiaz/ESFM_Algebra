import math as m

def fact():
	x = int(input("\na:\t"));i = 2
	print("\n\\begin{tabular}{ r | l }")
	while (i <= x):
		if (x % i == 0): x /= i; print("\t%i\t&\t%i\t\\\\" % (i,x))
		else: i += 1
	print("\\end{tabular}")


def mcd():
	A = a = int(input("\na:\t"))
	B = b = int(input("b:\t"))
	print("\n\\begin{align*}")
	while (b != 0):
		print("\t %i &= " % a, end='')
		d = a // b; c = b
		b = a %  b; a = c
		print("%i ( %i ) + %i \\\\" % (a,d,b))
	print("\\end{align*}")
	print("\n$$%i=\\textrm{MCD}(%i, %i)=%is+%it$$" % (a,A,B,A,B))

	mcd2(A,B,a)
	mcd2(B,A,a)

def mcd2(A,B,a):
	i = 1;d = 1
	while (d % B != 0):
		i += 1
		d = A * i - a
	print("$$%i = %i(%i) - %i(%i) $$" % (a,A,i,B,d/B))


def cuad():
	a = float(input("\na:\t"))
	b = float(input("b:\t"))
	
	print("\n\\begin{align*}")
	print("\t(x + yi)^2\t&=\t %f + %f i \\\\" % (a,b) )
	print("\tx^2 - y^2 + 2xyi\t&=\t %f + %f i \\\\\\\\" % (a,b) )
	
	print("\tx^2 - y^2\t&=\t%f \\\\" % a)
	print("\t2xy\t&=\t%f \\\\\\\\" % b)

	print("\t(x^2 - y^2)^2\t&=\t %f\\\\" % a**2)
	print("\t(2xy)^2\t&=\t %f \\\\\\" % b**2)

	print("\tx^4 - 2x^2y^2 + y^4\t&=\t %f \\\\" % a**2)
	print("\t4x^2y^2\t&=\t %f\\\\\\\\" % b**2)

	print("\tx^4 + 2x^2y^2 + y^4\t&=\t %f \\\\" % (a**2+b**2) )
	print("\t(x^2 + y^2)^2\t&=\t %f \\\\"% (a**2+b**2) )
	print("\tx^2 + y^2\t&=\t %f \\\\\\\\" % m.sqrt(a**2 + b**2))
	print("\\end{align*}\n")
	
	print("$$2x^2\t=\t%f+%f\t=\t%f$$" %( m.sqrt(a**2 + b**2), a, m.sqrt(a**2 + b**2) + a) )
	print("$$2y^2\t=\t%f-%f\t=\t%f$$"% ( m.sqrt(a**2 + b**2), a, m.sqrt(a**2 + b**2) - a) )


def raices():
	n = int(input("\nn:\t"))
	a = float(input("a:\t"))
	b = float(input("b:\t"))

	r = round(m.sqrt(a**2 + b**2), 2)
	
	if(a==0):t = 90
	else:t = round(m.degrees(m.atan(b / a)), 2)
	print("\n$$r=\\sqrt{%f^2+%f^2}=%f\t\\qquad\t\\theta=\\tan^{-1}\\left(\\frac{%f}{%f}\\right)=%f$$" % (a,b,r,b,a,t) )
	print("$$\\sqrt[n]{a+bi}\t=\\sqrt[%i]{%f}\\left(\\cos \\left(\\frac{%f+ 360 k }{%i}\\right) + i \\sin \\left(\\frac{%f+ 360 k }{%i}\\right)\\right)$$\n" % (n,r,t,n,t,n))

	for i in range(n):
		print("$$\\sqrt[%i]{ %f + %f i}\t=\\sqrt[%i]{%f}\\left(\\cos( %f + %f \\cdot %i ) + i \\sin( %f + %f \\cdot %i )\\right)=\\sqrt[%i]{%f}\\left(\\cos (%f) +i \\sin(%f)\\right)$$" % (n,a,b,n,r,t/n,360/n,i,t/n,360/n,i,n,r,(t+360*i)/n,(t+360*i)/n))

		
