valores_romanos ={
                  1: "I",
                  5: "V", 
                  9: "IX",
                  10: "X",
                  40: "XL",
                  50: "L", 
                  90: "XC",
                  100: "C",
                  400: "CD",
                  500: "D",
                  900: "CM",
                  1000: "M"}


 
 
#valores_romanosT = [(1000,"M"), (900, "CM"),(500,"D"), (400, "CD"), (100,"C"), (90, "XC"), (50,"L"), (40, "XL"),(10,"X"), (9, "IX"),(5,"V"), (1,"I")]
#ordenamos la lista en orden contrario para evitar que se nos salga siempre con el 1
 
def valida_numero (n):
    if not isinstance (n, int):
        raise TypeError (f" {n} debe ser de tipo int")
    if n <=0:
        raise ValueError (f"{n} debe ser un numero entero positivo")   #como te devuelve una xcepcion la funcion no lleva return






def arabigo_a_romano (n):  
    valida_numero()     
    romano = ""
    resto = 1    #hay que darle un valor arbitrario para que lo reconozca la función, que sólo tiene un parámetro que es n   
    #36    XXXVI   
    # desde for hasta la linea de resto = n% valor iria encima del while para evitar inicialr arbitrariamente el valor de resto = 1
    while resto > 0:
   
        for valor in sorted (valores_romanos.keys(), reverse = True):
            if n >= valor:
                break
        cociente = n // valor
        resto = n % valor
        romano += cociente * valores_romanos[valor] 
        n = resto
    return romano

print(arabigo_a_romano(46))




def romano_a_arabigo (cadena):
    resultado = 0
    for ix in range(len(cadena)-1):
        cadena = cadena[ix]
        siguiente = cadena[ix+1]
        if d[letra]>= d[siguiente]:
            resultado += d[letra]
        else:
            resultado -= d[letra]
    resultado += d[len(cadena)-1]            


