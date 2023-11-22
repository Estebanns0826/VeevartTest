## ESTEBAN RAMOS GOMEZ - PRUEBA VEEVART

## EN ESTE CODIGO SOLAMENTE SE ESTA TESTEANDO LA FUNCIONALIDAD DE LAS FUNCIONES DEL CODIGO
# DEL JUEGO POR LO QUE NO SE PONE COMPLETO

import random

# Funciones del juego
def dado(continuar):
    while True:
        if continuar.lower() == "si":
            valor_maximo = 6
            valor_minimo = 1
            valor_dado = random.randint(valor_minimo, valor_maximo) # SE INGRESA LA FUNCION DE LOS DADOS - SE TIRA DADOS
            return valor_dado
        else:
            continuar = input("Por favor, ingresa 'si' para tirar el dado: ")

def mover_jugador(pos_jugador, valor_dado):
    pos_jugador += valor_dado

    if pos_jugador >= 25:
        return "Eres el mejor, has ganado"
    elif pos_jugador == 4:
        pos_jugador = 18 # Prueba la escalera 
  

    return pos_jugador

# Pruebas unitarias
def test_dado_si():
    assert dado("si") in range(1, 7)  ## TESTEA SI EL DADO ESTA DENTRO DE LOS VALORES DE RANGO (1 A 6)
    print("test dados pasado")



def test_mover_jugador():
    assert mover_jugador(0, 4) == 18  ## TESTEA EL MOVIMIENTO DEL JUGADOR - PRUEBA LA ESCALERA
    print("test movimiento jugador pasado")
 
    # Agregar más pruebas para otras situaciones...

# Ejecución de las pruebas
test_dado_si()
test_mover_jugador()