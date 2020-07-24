#w3school
#tutorialesya
"""
saludo = "Hola Clase"
asignatura = "TIII"
anho = 2020
semestre = 1

print(saludo + " " + asignatura + " " + str(anho) + "-" + str(semestre))

entrada = input("Ingrese un valor")
numero = int(entrada)
print("El valor ingresado es: " + str(numero))
"""
# operaciones numericas
# Suma +
# resta -
# multiplicacion *
# Division /
# Modulo % -> resto de la division
# Division entera // -> la parte entera del cociente -> 9/2 = 4.5 -> 9//2 = 4
# potencia ** -> 4**2 = 16
"""
a = int(input("Ingrese valor: "))
b = int(input("Ingrese valor: "))

r = a ** b

print("El resultado es: "+ str(r))
"""
# Operaciones en Strings -> Cadenas

cadena = "Este es un ejemplo de String"
# [posicion]
# [desde: hasta(n-1)]
# [posicion negativa]
# [desde negativo: hasta negativo]
# Rangos incompletos
#print("En caracter es: " + cadena[:10])

# lower() para minusculas
# upper() para mayusculas
# replace(caracter a buscar, caracter a reemplazar)
#print("String: " + cadena.replace("String", "Cadena"))

# split(caracter para dividir) -> dividir un string
palabras = cadena.split(" ")
print(palabras)
print("String: " + palabras[0])
