#ejercicio 1
lado1 = float(input("Ingrese el primer lado"))
lado2 = float(input("ingrese el segundo lado"))
lado3 = float(input("ingrese el tercer lado"))

if lado1 <= 0 or lado2 <= 0 or lado3 <=0:
    print("error: todos los lados deben ser mayores que cero")
else:
    if (lado1 + lado2 > lado3 ) and (lado1 + lado3 > lado2 ) and (lado2 + lado3 > lado1):

     print("los lados ingresados forman un triangulo valido.")
    if lado1 == lado2 == lado3:
        tipo = "equilatero"
    elif lado1 == lado2 or lado1 ==lado3 or lado2 == lado3:
        tipo = "isosceles"
    else:
        tipo = "escaleno"
    print(f"tipo de triangulo: {tipo}.")
    
print("Los lados ingresados no forman un triangulo")