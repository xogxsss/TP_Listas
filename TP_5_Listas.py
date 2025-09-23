#1. Crear una lista con los números del 1 al 100 que sean múltiplos de 4. 
# Utilizar la función range

lista = []
i = 0

for i in range(4, 101, 4):
    lista.append(i)

print(lista)

#2. Crear una lista de 5 elementos, mostrar el penúltimo con indexing de números negativos

lista = [1, 2, 3, 4, 5, 6]
penultimo = lista[-2]

print(penultimo)

#3. Crear una lista vacía, agregar tres elementos con append()

frutas = []

frutas.append("banana")
frutas.append("manzana") #append toma un elemento, así que los agregamos uno a uno
frutas.append("naranja")
print(frutas)

#4. Reemplazar el segundo y último valor de la lista con "loro" y "oso".

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#6. Crear una lista con números del 10-30 (incluído), con paso 5; mostrar los dos primeros

lista = []
for i in range(10, 31, 5):
    lista.append(i)

print(lista)

#7. Reemplazar los dos valores centrales por dos valores nuevos

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camineta", "hatchback"]
print(autos)

#8. Crear una lista vacía y agregar el doble de 5, 10 y 15 usando append directamente

dobles = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)

print(dobles)

#9. Dada la lista "compras":
# - Agregar "jugo" a la lista del tercer cliente con append
# - Reemplazar "fideos" por "tallarines" 
# - Eliminar "pan"
# - Imprimir la lista resultante

compras = [
    ["pan", "leche"], 
    ["arroz", "fideos", "salsa"], 
    ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#10. Elaborar una lista anidada con los siguientes elementos:
# Posición lista_anidada[0]: 15 
# Posición lista_anidada[1]: True 
# Posición lista_anidada[2][0]: 25.5 
# Posición lista_anidada[2][1]: 57.9 
# Posición lista_anidada[2][2]: 30.6 
# Posición lista_anidada[3]: False

lista_anidada = [
    [15],
    [True],
    [25.5, 57.9, 30.6],
    [False]
]

print(lista_anidada)