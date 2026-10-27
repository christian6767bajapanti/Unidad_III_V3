#ejercicio2
cantidad = int(input("¿cuantos numeros desea analizar?: "))

if cantidad <= 0:
    print("error: la catidad de numeros debe ser un entero mayor que cero")
else: 
    positivos = 0
    negativos = 0
    ceros = 0
    suma_total = 0
    
    for i in range(1, cantidad + 1):
        num = float(input(f"ingrese el numero {i}: "))
        suma_total += num
        if num > 0:
            positivos  += 1
        elif num < 0:
            negativos += 1
        else:
            ceros += 1
        
promedio = suma_total / cantidad 

print (f"cantidad de positivos : {positivos}")  
print (f"cantidad de negativos : {negativos}")
print (f"cantidad de ceros: {ceros}")
print (f" suma total: {suma_total:g}")
print (f"promedio: {promedio:.2f}")