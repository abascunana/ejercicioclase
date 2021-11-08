def cercar(text,cadena):
   contador=0
   for i in range(len(text) -(len(cadena)-1)):
      j=0
      while j<len(cadena):
         if text[i+j]==cadena[j]:
            j=j+1
            if j == len(cadena):
               contador = contador + 1             
         else:
            j=len(cadena)
   return(contador)

t=input("introdueix text:")
p=input("introdueix paraula:")

print(cercar(t,p))
