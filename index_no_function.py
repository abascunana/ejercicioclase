def indexse(palabra,x): #esta función hace lo mismo que el index()
    
    for i in range(len(x)): # bucle que revisa la largaria de lista x
        if x[i] in palabra: #si lista x(se tiene que cambiar) contiene el elemento "palabra",printea la posción
           a = ("elemento localizado en posición",i)
    if x[i] not in palabra:
        a = "no localizado"
    return(a) #print x para comprobar

print(indexse("84",["8","82","84"]))
