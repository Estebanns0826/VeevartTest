# AUTOR: ESTEBAN RAMOS GOMEZ
# PRUEBA: VEEVART 22 DE NOVIEMBRE DEL 2023

import random
pos_jugador = 0
print("Bienvenidos al juego de escaleras y serpientes (CREADO O DISEÑADO POR ESTEBAN RAMOS GOMEZ)")
#La función dado se implementa para que el usuario siga tirando el dado hasta llegar a su posición final
import random
# Función que realiza el tiro del dado
def dado(continuar):
    # Validación para asegurarse de que el usuario ingrese una opción válida
    while True:
        if continuar.lower() == "si":
            valor_maximo = 6  # Valor máximo del dado
            valor_minimo = 1  # Valor mínimo del dado
            valor_dado = random.randint(valor_minimo, valor_maximo)  # Se genera el tiro del dado
            print("Has tirado el dado y has sacado: " + str(valor_dado))
            return valor_dado  # Retorna el tiro del dado
        else:
            continuar = input("Por favor, ingresa 'si' para tirar el dado: ")

while pos_jugador <= 24:
    valor_dado = dado(continuar=(input("\n ¿Desea tirar el dado? \n"))) # Pregunta al usuario por el tiro dado
    pos_jugador = pos_jugador + valor_dado
    print("Actualmente estas en la posición : " +str(pos_jugador))

    if (pos_jugador >= 25):
          print("HAS GANADO, ERES EL MEJOR DEBIDO A QUE HAS PASADO LA POSICIÓN 25") # Anuncia la victoria del jugador
# Escaleras de para subir en el tablero
    if pos_jugador == 4:
          pos_jugador = 18
          print ("has subido a la posición " +str(pos_jugador) + " por una escalera") 
          print ("actualmente estas en la posición : "+str(pos_jugador))

    if pos_jugador == 6:
          pos_jugador = 9
          print ("has subido a la posición " +str(pos_jugador) + " por una escalera")
          print ("actualmente estas en la posición : "+str(pos_jugador))

    if pos_jugador == 2:
          pos_jugador = 16
          print ("has subido a la posición " +str(pos_jugador) + " por una escalera")
          print ("actualmente estas en la posición : "+str(pos_jugador))
          
    if pos_jugador == 19:
          pos_jugador = 23
          print ("has subido a la posición " +str(pos_jugador) + " por una escalera")
          print ("actualmente estas en la posición : "+str(pos_jugador))
# Serpientes, hacen bajar la posición actual del jugador
    if pos_jugador == 5:
          pos_jugador = 2
          print("RAYOS has caido por una serpiente hasta la posición : "+str(pos_jugador))
          print ("actualmente estas en la posición : "+str(pos_jugador))

    if pos_jugador == 17:
          pos_jugador = 17
          print("RAYOS has caido por una serpiente hasta la posición : "+str(pos_jugador))
          print ("actualmente estas en la posición : "+str(pos_jugador))

    if pos_jugador == 19:
          pos_jugador = 14
          print("RAYOS has caido por una serpiente hasta la posición : "+str(pos_jugador))
          print ("actualmente estas en la posición : "+str(pos_jugador))

    if pos_jugador == 13:
          pos_jugador = 6
          print("RAYOS has caido por una serpiente hasta la posición : "+str(pos_jugador))
          print ("actualmente estas en la posición : "+str(pos_jugador))
 
    if pos_jugador == 17:
          pos_jugador = 13
          print("RAYOS has caido por una serpiente hasta la posición : "+str(pos_jugador))
          print ("actualmente estas en la posición : "+str(pos_jugador))


