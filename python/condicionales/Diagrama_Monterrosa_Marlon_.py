
"""Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores
a “1.500.000” mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
y muestre por pantalla si el usuario tiene que tributar o no."""


edad = int(input("Por favor, ingrese su edad: "))
ingresos = float(input("Por favor, ingrese sus ingresos mensuales en pesos colombianos: "))

    
if edad >= 18 and ingresos >= 1500000:
        print("Usted debe tributar.")
else:
        print("Usted no tiene que tributar.")

