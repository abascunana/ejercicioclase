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


def enter(numero):  
    #esta array 
    simbolos = ["0","1","2","3","4","5","6","7","8","9"]
    #resultado final
    resultado = 0
    # bucle que recorre la totalidad de símbolos
    for i in range(len(simbolos)): #i es igual a los valores del range de simbolos en cada bucle
            j=0
            # bucle que comprueba que j no sea mayor a la posición de símbolos,esto para indicar que el
            # programa termine en algún momento (cuando se hayan recorrido todos los símbolos) 
            # valor de el número introducido coincide con los símbolos y hace cáculo
            # de otra forma le suma 1 a j y vuelve a comenzar el bucle while
            while j < len(simbolos):
                if numero[i] == simbolos[j]:
                    #si la posición actual del número es igual a la posición de símbolos hace esto 
                    #en este cálculo se suma al resultado j por 10 elevado a la largaria del nunmero introducido,si el valor fuera 150
                    #haría 0 + 1 * 10 ** 2, eso daría 100, después 100 + 5 * 10 ** 1, y ahí daría 150
                    
                    resultado = resultado + j * 10**(len(numero) - 1 - i)
                    # j es igual al número que sale en la posición que revisa el bucle,es decir, si el número fuera 150
                    # y el bucle estuviera en la posición 0 por defecto, j sería 1
                    j=len(simbolos)
                else:
                    #en este apartado suma 1 a j por cada posición no coincidente y se vuelve a al while, esto para hacer que el programa avance posiciones a partir 
                    #del 0
                    j=j+1
            return(resultado,type(resultado))
            

print(enter(input("introduce un número ")))


