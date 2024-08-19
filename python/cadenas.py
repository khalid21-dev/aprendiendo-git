v1 = "marlon"
v2 = "khalid"

#concatenación

print(v1 + ", "+ v2 + "!")

#Repetición

print(v1 * 5)

# Indexación
print(v2[0] + v2[1] + v1[1] + v1[3] + v2[4] + v2[5])

# Logitud

print(len(v2))

# slicing (Porción)

print(v1[:3])
print(v2[2:])

#Busqueda

print ("r" in v1)
print ("x" in v2)

#Reemplazo 
print(v1.replace("r", "i"))

# División de cadenas de caracteres
print(v2.split("l"))

# Mayúsculas, minúsculas y letras en Mayúsculas

print(v2.upper())
print(v2.lower())
print("marlon monterrosa".title())#primera letra en mayusculas de cada palabra
print("marlon monterrosa".capitalize())# solo la primera letra de la 1 palabra

# Eliminación de espacios al principio y al final 

print(" marlon monterrosa ".strip())

#Busqueda al principio y al final
print(v2.startswith("ma"))
print(v2.startswith("kh"))
print(v2.endswith("kh"))
print(v2.endswith("id"))

# Búsqueda de psosición

print("marlon monterrosa muñoz".find("mon"))
print("marlon monterrosa muñoz".find("ñoz"))
print("marlon Monterrosa muñoz".find("M"))
print("marlon monterrosa muñoz".find("m"))

#Búsqueda de ocurrencias

print("marlon monterrosa muñoz".lower().count("m"))

#Formateo

print("name: {}, apodo: {}!".format(v1,v2))

# interpolación

print(f"name: {v1}, apodo: {v2}")

#Tranformación en lista de caracteres 

print(list("marlon monterrosa muñoz"))

# Tranformación de la lista de cadena

l1 = [v1, ", ", v2 , "!"]
print("".join(l1))

#Tranformaciones numéricas
v4 = "123456"
v4 = int(v4)
print(v4)

v5 = "123456.123"
v5 = float(v5)
print(v5)

#Comprobaciones varias

v6 = "12345678"

print(v1.isalnum())
print(v1.isalpha())
print(v1.isalpha())
print(v1.isnumeric())

