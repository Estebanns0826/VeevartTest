
# PROBLEMAS DE REINAS NXN EN PYTHON
# ESTEBAN RAMOS GOMEZ
# PRUEBA VEEVART

# Función para verificar si es seguro colocar una reina en una posición específica
def revisar_seguridad_reina(tablero, fila, columna):
    for i in range(columna): # Recorre el valor el tamaño de la columna
        # Verifica si hay una reina en la misma fila o en diagonales
        if tablero[i] == fila or tablero[i] - i == fila - columna or tablero[i] + i == fila + columna:
            return False
    return True

# Función para imprimir el tablero con reinas (X) y espacios vacíos (O)
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join('(X)' if i == fila else '(O)' for i in range(len(tablero)))) ## REALIZA LA MATRIZ RELLENANDO X Y O PARA LAS REINAS
    print("\n")

# Función auxiliar para resolver el problema de las N reinas
def resolver_n_reinas_util(tablero, columna, n):
    # Si todas las reinas se han colocado en columnas, muestra la solución
    if columna == n:
        imprimir_tablero(tablero)
        return
    
    # Intenta colocar una reina en cada fila de la columna actual
    for fila in range(n):
        if revisar_seguridad_reina(tablero, fila, columna):
            tablero[columna] = fila
            resolver_n_reinas_util(tablero, columna + 1, n)

# Función principal para resolver el problema de las N reinas
def resolver_n_reinas(n):
    tablero = [-1] * n  # Inicializar el tablero con los valores predeerminados
    resolver_n_reinas_util(tablero, 0, n)  # Comienza con la columna 0

# Se realiza el llamado de la función 'resolver_n_reinas()' 4x4
resolver_n_reinas(4)