# Estructuras de Control
"""
Operadores Relacionales
== igual
!= no es igual
<  menor
>  mayor
<= menor igual
>= mayor igual

Operadores Logicos
and -> y logico -> &&
or  -> o logico -> ||
not -> negacion -> !

Operadores de identidad
is     -> pertence a 
is not -> no pertenece

Operadores de membresia
in     -> aparece en 
not in -> no aparece en 
"""


# Bifurcacion (if)

#edad = int(input("Ingrese su edad: "))
"""
if edad >= 18 :
    print("Usted es Mayor de Edad")
    print("Sigo en el if")
    if edad >= 60:
        print("Usted es Adulto Mayor")
else:
    print("Usted Es Menor de Edad")

print("Sigo fuera del if")
"""
# Ciclos
# while (mientras)

"""
while edad > 0:
    print("valor: " + str(edad))
    #edad = edad - 1
    edad -= 1
"""
# for (iterable)
# for variable_iteracion in variable_iterable:
"""
variable_iterable = ["azul", "rojo", "negro", "gris", "blanco"]

for i in variable_iterable:
    print("Valor: " + str(i))
"""
# range(n) -> [0,n-1]
# range(n,m) -> [n, m-1]
for i in range(1,10):
    print("Valor: " + str(i))
