animales = ["lobo","perro","vaca","pez","gato"]

numeros = [12,23,45,36,34]

#recorriendo la lsista de animales
for animal in animales:
    print(f'ahora la variable animal es igual a:{animal}')

#recorriendo la lista de numeros y multiplicando por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo
for animal,numero in zip(animales,numeros):
    print(f'recorriendo lista 1:{animal}')
    print(f'recorriendo lista 2:{numero}')

#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = [0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es :{valor}')

#usando el else
for numero in numeros:
    print(f"ejecuntando el ultimo bucle, valor actual:{numero}")
else:
    print("el bucle termino")
    
#todo lo anterior fum¡nciona para las tuplas funciona igual para ellas 