def enter(numero):  
    #esta array 
    simbolos = ["0","1","2","3","4","5","6","7","8","9"]
    #resultado final
    resultado = 0
    # bucle que recorre la totalidad de símbolos
    for i in range(len(simbolos)): #i recorre los valores del range de simbolos en cada bucle
            #j es igual a 0 para que éste empiece en la primera posición del número introducido, es decir si el número fuera 150 la posición 0 sería "1"
            j=0
            # bucle que comprueba que j no sea mayor a la posición de símbolos,esto para indicar que el
            # programa termine en algún momento (cuando se hayan recorrido todos los símbolos) 
            # valor de el número introducido coincide con los símbolos y hace cáculo
            # de otra  forma (else) le suma 1 a j para avanzar posición en el número introducido y vuelve a comenzar el bucle while
            while j < len(simbolos):
                if numero[i] == simbolos[j]:
                    #si la posición actual del número es igual a la posición de símbolos hace esto (cálculo de abajo)
                    #en este cálculo se suma al resultado j por 10 elevado a la largaria del número introducido,si el valor fuera 150
                    #haría 0 + 1 * 10 ** 2, eso daría 100, después 100 + 5 * 10 ** 1, y ahí daría 150
                    
                    resultado = resultado + j * 10**(len(numero) - 1 - i)#se resta -1 -i para que eleve la cantidad necesaria tras cada número recorrido, es decir, si se pone 525
                    #que no haga 5 * 10 ** 3,sino 5 *10 **2,y después 2 * 10 ** 1, en el punto de llegar al 20 el bucle habría sido recorrido una vez,por lo que i igualaría a 1
                   
                    # j es igual al número que sale en la posición que revisa el bucle,es decir, si el número fuera 150
                    # y el bucle estuviera en la posición 0 por defecto, j sería 1
                    j=len(simbolos)
                else:
                    #en este apartado suma 1 a j por cada posición no coincidente y se vuelve a al while, esto para hacer que el programa avance posiciones a partir 
                    #del 0
                    j=j+1
            return(resultado,type(resultado))
            

print(enter(input("introduce un número ")))


