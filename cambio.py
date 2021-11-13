#en esta lista están los billetes que la máquina admite
ma = [5, 10, 20, 50, 100, 200, 500]
bil = int(input("introduce la cantidad que quiera devolver en cambio "))
#en esta lista se registran los resultados de cambio de la máquina
y=[]
#bucle que revisa 7 veces el resultado de dividir el cambio pedido por todas la opciones disponibles
i= 0
for i in range (ma[i]):
  a=int(bil/ma[i])
  #condicional que revisa si el resultado de "y" sea mayor
  # a 0 y que de una cantidad de cambio buena, si se cumple, se registra en "y"
  
  if a > 0 and (bil%ma[i])==0:
     y.append(a)
# condicional que cambia entre el plural y singular
    
     if min(y) == 1:
       print(i+1,"opcion la máquina te devuelve",min(y),"billete de",ma[i],"euros")       
     else:
       print(i+1,"opcion la máquina te devuelve",min(y),"billetes de",ma[i],"euros")
i +=1
