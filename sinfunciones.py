def insertar(posicion,valor,lista):
    #lista vacíá en la que se almacenará el resultado
    resultat=[]
    #bucle que recorre toda la largaria de la lista que introduzca el usuario
    for i in range (len(lista)):
        #si el número de veces en las que se ha recorrido lista es igual a 
        #la posición introducida por el usuario. Realiza el cálculo 
        #en el cálculo se   indica que resultado se concatena con valor 
        if i == posicion:
            resultat= resultat + [valor]
        #fuera de if, resultado es igual a la lista que del usuario + el resultado del if
        resultat=resultat+[lista[i]]
    return resultat








def enter(numero):  
    #esta array 
    simbolos = ["0","1","2","3","4","5","6","7","8","9"]
    #resultado final
    resultado = 0
    # bucle que recorre la totalidad de símbolos
    for i in range(len(simbolos)): #devuelve los valores del range de simbolos
            j=0
            # bucle que comprueba que j no sea mayor a la posición de símbolos,esto para indicar que el
            # programa termine en algún momento (cuando se hayan recorrido todos los símbolos) 
            # valor de el número introducido coincide con los símbolos y hace cáculo
            # de otra forma le suma 1 a j y vuelve a comenzar
            while j < len(simbolos):
                if numero[i] == simbolos[j]:
                    #si la posición actual del número es igual a la posición de símbolos hace esto 
                    #en este cálculo se suma al resultado j por 10 elevado a la largaria del nunmero introducido
                    resultado = resultado + j * 10 ** len(numero)-1-i
                    # j es igual a la largaria de los símbolos,cuando
                    j=len(simbolos)
                else:
                    #en este apartado suma 1 a j por cada posición no coincidente y se vuelve a al while
                    j=j+1
            print(resultado) 
print(insertar(1,"aa",["1","2"]))
