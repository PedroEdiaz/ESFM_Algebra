import algebra as a
import math as m
def fillPolin(f):
	n=int(input("\nDe que grado es el polinomio?\t"))
	for i in range(n+1):
		f.append(complex(input("x^%i=\t" % (n-i))))
		
def clean(txt):
	txt=txt.replace("+0j","")
	txt=txt.replace("-0j","")
	txt=txt.replace("+1x","+x")
	txt=txt.replace("-1x","-x")
	txt=txt.replace("(","")
	txt=txt.replace(")","")
	txt=txt.replace("x^{1}","x")
	txt=txt.replace("x^{0}","")
	txt=txt.replace("j","i")
	txt=txt.replace("+-","-")
	txt=txt.replace("}x^{","}+0x^{")
	return txt

def form(g):
	j=0; txt=''
	for i in g:
		j+=1
		txt+='+%sx^{%i}' % (i,len(g)-j)
	return clean(txt)

def divPolin(f,g):
	print()

	f0=[""]
	for i in f:
		f0+=[round(i.real, 2) + round(i.imag, 2) *1j ]
	
	maxf=len(f);maxg=len(g);div=[]
	for i in range(maxf-maxg+1):
		q=f[i]/g[0]
		aux=[round(q.real, 2)+round(q.imag, 2) *1j]+[""]*i
		for j in g:	
			aux+=[round((-q*j).real, 2) + round((-q*j).imag, 2) *1j ]
		div.append(aux)
		for j in range(len(g)):
			f[j+i]-=round((q*g[j]).real, 2) + round((q*g[j]).imag, 2) *1j	
		aux=[""]*(i+2)
		for j in range(maxg-1): 
			aux+=[round((f[j+i+1]).real, 2) + round((f[j+i+1]).imag, 2) *1j ]
		div.append(aux)
		
	q=[]
	print("\n\\begin{center}\n\\begin{tabular}{ r %s}" % ("c "*maxf) )
	for i in range(0,len(div),2):
		q.append(div[i][0])
		print("\t& $%s$ " % clean("%sx^{%i}" % (div[i][0],(int((len(div)-i)/2-1)))) , end='')
	print("\t\\\\ \\cline{2-%i}" % (maxf+1))
	print("$",form(g),end=" \\big|$")
	for i in range(1,len(f0)):
		print("\t& $%s$ " % clean("%sx^{%i}" % (f0[i],maxf-i)) , end='')
	print("\\\\")
	n=1
	for i in div:
		
		for j in range(len(i)):
			if(j != 0):
				if ( i[j] != '' ):
					print("\t& $%s$ " % clean("%sx^{%i}" % (i[j],maxf-j)),end='')
				else:
					print("\t&",end='')
		print("\\\\")
		if(n%2):
			print("\\cline{%i-%i}" % (n/2+2,n/2+len(g)+1))
		n+=1

	print("\\end{tabular}\n\\end{center}\n")

	return(aux[len(f)-len(g)+2:])

def sintetica(f,g):
	aux1=[-g[1]/g[0],0]
	aux2=[0,f[0]]
	for i in range(1,len(f)):
		aux=round((aux2[i]*aux1[0]).real,3)+round((aux2[i]*aux1[0]).imag,3)*1j
		aux1.append(aux)
		aux2.append(f[i]+aux1[i+1])
		
	print("\n\\begin{center}\n\\begin{tabular}{ r | %s}" % ("c "*(len(f)+1)) )
	for i in f:print("\t& $%s$" % (clean(str(i))),end='')
	print("\\\\")
	for i in aux1:print("$%s$" % (clean(str(i))),end='\t&')
	print("\\\\ \\hline")
	for i in range(1,len(aux2)):
		print("\t&", end='')
		if(i==len(aux2)-1):print("\\big|",end='')
		if(i!=0): print("$%s$" % (clean(str(aux2[i]))),end='')
		
	print("\\\\")
	print("\\end{tabular}\n\\end{center}\n")

	return [ i for i in aux2 ]

def mcd(f,g):
	while True:
		r=g
		g=divPolin(f,g)
		f=r

		while (g[0]==0j and len( g)>1):
			g.pop(0)	
			
		if(len( g)==1):break
			
	
def raices(f):
  print("\n$$f(x)=\t%s$$"%form(f))
  a0=f[0]
  an=f[-1]

  g=[]
  k=[]
  print("\nDivisores de $a_0$:",end="\t")
  for i in range(int(abs(a0)+1)):
    aux=a0/(i+1)
    if (aux.real%1==0 and aux.imag%1==0):
      g.append(i+1)
      print(i+1,end=', ')

  print("\\\\\nDivisores de $a_n$:",end="\t")
  for i in range(int(abs(an)+1)):
    aux=an/(i+1)
    if (aux.real%1==0 and aux.imag%1==0):
      k.append(i+1)
      print(i+1,end=', ')

  root=[]
  print("$$\n\n\\begin{align*}")
  for i in g:
    for j in k:
      test=round(a.Comp(f,[j/i])[0].real,2)
      print("\tf({}/{})&= {}\t&".format(j,i,test),end="")
      if test==0:
        root.append("{}/{}".format(j,i))
        
      test=round(a.Comp(f,[-j/i])[0].real,2)
      print("\tf(-{}/{})&= {} \\\\".format(j,i,test))
      if test==0:
        root.append("-{}/{}".format(j,i))
  print("\\end{align*}")
  
  print("\nRaices: ",end="\t")
  for i in root: 
    print (i,end=", ")

    while(a.Comp(f,[eval(i)])==[0j]):
      f=sintetica(f,[1,-eval(i)])
      f.pop(); f.pop(0)
      
  
  if(input("\n\nProbar Imáginarios?(s/n): ")=="s"):
    print("\nDivisores de $a_0$:",end="\t")
    for i in range(int(abs(a0)+1)):
      for j in range(1,int(abs(a0)+1)):
        if (0 < abs(i+j*1j) ):
          aux=a0/(i**2+j**2)
          if (aux.real%1==0 and aux.imag%1==0):
            g.append(i+j*1j)
            print(i+j*1j,end=', ')
            g.append(i-j*1j)
            print(i-j*1j,end=', ')

    print("\\\\\nDivisores de $a_n$:",end="\t")
    for i in range(int(abs(an)+1)):
      for j in range(1,int(abs(an)+1)):
        if (0 < abs(i+j*1j) ):
          aux=an/(i**2+j**2)
          if (aux.real%1==0 and aux.imag%1==0):
            k.append(i+j*1j)
            print(i+j*1j,end=', ')
            k.append(i-j*1j)
            print(i-j*1j,end=', ')


  print("$$\n\n\\begin{align*}")
  for i in g:
    for j in k:
      if((j/i).imag!=0):
        test=round(a.Comp(f,[j/i])[0].real,2)
        print("\tf({}/{})&= {}\t&".format(j,i,test),end="")
        if test==0:
          root.append("{}/{}".format(j,i))
        
        test=round(a.Comp(f,[-j/i])[0].real,2)
        print("\tf(-{}/{})&= {} \\\\".format(j,i,test))
        if test==0:
          root.append("-{}/{}".format(j,i))
    print("\\end{align*}")
  
  print("\nRaices: ",end="\t")
  for i in root: 
    print (i,end=", ")

    while(a.Comp(f,[eval(i)])==[0j]):
      f=sintetica(f,[1,-eval(i)])
      f.pop(); f.pop(0)
