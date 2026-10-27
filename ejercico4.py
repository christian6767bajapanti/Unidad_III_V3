#ejercicio 4

clave = input ("ingrese una contraseña :")

longitud_valida = len(clave) >= 8
tiene_mayus = False
tiene_minus = False
tiene_num = False
tiene_espacio = False

for char in clave:
    if char.isupper ():
        tiene_mayus = True
    if char.islower():
        tiene_minus = True
    if char.isdigit():
        tiene_num = True
        
    if char.isspace():
        tiene_espacio = True
    
criterios_cumplidos = 0
if longitud_valida:
    criterios_cumplidos += 1
if tiene_mayus:
    criterios_cumplidos += 1
if tiene_minus:
    criterios_cumplidos += 1
if tiene_num:
    criterios_cumplidos +=1
    
if tiene_espacio:
    clasificacion = "debil"
else:
    if criterios_cumplidos == 4:
        clasificacion = "fuerte"
    elif criterios_cumplidos == 3:
        clasificacion = "aceptable" 
    else:
        clasificacion = "debil"
        
print(f"longiud: {len(clave)}")
print(f"contiene mayuscula: {'si' if tiene_mayus else 'no'}")
print(f"contiene minuscula: {'si' if tiene_minus else 'no'}")
print(f"contiene_numero: {'si' if tiene_num else 'no'}")
print(f"contiene espacios: {'si' if tiene_espacio else 'no'}")
print("criterios cumplidos: {criterios_cumplidos} de 4")
print(f"clasificaion: {clasificacion}")