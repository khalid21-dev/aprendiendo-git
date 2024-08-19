ingreso_mensual = int(input("digite cuanto gana mensualmente>:"))

if ingreso_mensual > 10000000:
    print("ERES RICO")

if ingreso_mensual > 5000000:
    print("estas bien economicamente")
    
elif ingreso_mensual > 1500000:
    print("ganas mas del minimo")

elif ingreso_mensual > 600000:
    print("ganas muy poco")
    
else:
    print("eres pobre")

