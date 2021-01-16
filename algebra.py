def Sum(f,g):
  if(len(f)>len(g)):
    aux=f;sum=g
  else:
    sum=f;aux=g
  for i in range(len(sum)):
    aux[i-len(sum)]+=sum[i]
  return aux

def Mult(a,b):
  aux=[]
  for i in range(len(b)):
    mult=[]

    for j in range(len(a)):
      mult.append(b[i]*a[j])
  
    for j in range(len(b)-i-1):
      mult.append(0)

    aux=Sum(aux,mult)

  return aux

def Exp(f,n):
  aux=[]
  for i in f:
    aux.append(i)
  if (n==0):
    return [1]
  else:
    return Mult(aux,Exp(aux,n-1))

def Comp(f,g):
  aux=[0]
  for i in range(len(f)-1):
    mult=Mult([f[i]],Exp(g,len(f)-i-1))
    aux=Sum(aux,mult)
  aux[-1]+=f[-1]
  return aux

def Deriv(f):
  aux=[]
  for i in f:
    aux.append(i)

  for i in range(len(aux)):
    aux[i]*=len(aux)-i-1

  try:
    aux.pop()
  except:
    aux=[]

  return aux

def Form(f,n):
  str=''
  for i in range(len(f)):
    aux=round(f[i].real)+round(f[i].imag,n)*1j
    str+='+{}x^{}\t'.format(aux,len(f)-i-1)
  return str.replace('+-','-')

def Div(f,a): #f(x)=(x-a)q(x)
  aux=Comp(f,[1,a])
  aux.pop()
  aux=Comp(aux,[1,-a])
  return aux