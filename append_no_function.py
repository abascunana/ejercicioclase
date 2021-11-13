def insertar(posicion,valor,lista):
    #lista vacíá en la que se almacenará el resultado
    resultat=[]
    #bucle que recorre toda la largaria de la lista que introduzca el usuario
    for i in range (len(lista)):
        #si el número de veces en las que se ha recorrido lista es igual a 
        #la posición introducida por el usuario. Realiza el cálculo 
        #en el cálculo se   indica que resultado se concatena con 
        #valor en el caso de que la posición indicada coincida con la posición recorrida en el bucle
        if i == posicion:
            resultat= resultat + [valor] #valor se pone entre corchetes porque se almacena como una lista
        # fuera de if,el resultado es igual a la lista que del usuario + el resultado del if
        resultat=resultat+[lista[i]]
    return resultat


print(insertar(1,"aa",["1","2"]))




