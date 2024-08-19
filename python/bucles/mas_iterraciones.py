#creando las listas
frutas =["banana","manzana","ciruela","pera","naranja","granadilla","durazno"]
cadena = "hola marlon"
numeros = [2,5,8,10]
#evitando comer una manzana con la sentencia (continue)

for fruta in frutas:
    if fruta=='manzana':
        continue
    print(f'm voy a comer una {fruta}')
    
print("-------------------")
#evitando que el bucle siga con (break) el else no se ejecuta porque esta el break
for fruta in frutas:
    print(f'm voy a comer una {fruta}')
    if fruta=='naranja':
        break
else:
    print("bucle terminado")

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)