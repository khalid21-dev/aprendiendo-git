#creando un contador que va a ir sumandose
contador = 1

#mientras la condicion se cumpla, el bucle se a seguir ejecutando
#(vuelta, tras vuelta se verifica la condición)

while contador < 32:
    contador += 2
    print(contador)

#manejo de excepciones 

try:
    print(20/0) #si esto es erroeneo
except:
    print("esto es erroneo")# el progrma no se va a petar si noq ue ejecutara "esto es erroneo"
finally:
    print("ha finalizado el codigo") #termina el codigo