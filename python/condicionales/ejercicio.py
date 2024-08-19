
'''
edad = int(input("dime tu edad > "))

if edad >= 18:
     print("eres mayor de edad")
     
else:
     print("eres menor de edad")
     
'''
'''
def mostrar_edades_cumplidas(edad):
    print("¡A continuación se muestran todos los años que has cumplido hasta ahora!")
    for i in range(1, edad + 1):
        print("Has cumplido", i, "años")

def main():
    edad = int(input("Por favor, introduce tu edad: "))
    mostrar_edades_cumplidas(edad)

if __name__ == "__main__":
    main()
'''







def tributacion():
    edad = int(input("Por favor, ingrese su edad: "))
    ingresos = float(input("Por favor, ingrese sus ingresos mensuales en pesos colombianos: "))

    if edad >= 18 and ingresos >= 1500000:
        print("Usted debe tributar.")
    else:
        print("Usted no tiene que tributar.")

tributacion()
