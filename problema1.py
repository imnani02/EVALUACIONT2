
PUNTOS_MINIMOS = 23
N = 9

laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visitado = [[False] * N for i in range(N)]
camino = []


def imprimir_laberinto(matriz):
    for fila in matriz:
        print(fila)


def valor(fila, columna):
    if laberinto[fila][columna] == 'I':
        return 1
    if laberinto[fila][columna] == 'F':
        return 1
    return laberinto[fila][columna]


def es_valida(fila, columna):
    if fila < 0 or fila >= N:
        return False

    if columna < 0 or columna >= N:
        return False

    if laberinto[fila][columna] == 0:
        return False

    if visitado[fila][columna]:
        return False

    return True


def buscar_camino(fila, columna, puntos):
    visitado[fila][columna] = True
    camino.append((fila, columna))

    puntos += valor(fila, columna)

    if fila == 0 and columna == 0:
        if puntos >= PUNTOS_MINIMOS:
            return True

        visitado[fila][columna] = False
        camino.pop()
        return False

    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]

        if es_valida(nueva_fila, nueva_columna):
            if buscar_camino(nueva_fila, nueva_columna, puntos):
                return True

    visitado[fila][columna] = False
    camino.pop()

    return False


def mostrar_solucion():
    solucion = []

    for fila in range(N):
        nueva_fila = []

        for columna in range(N):
            if laberinto[fila][columna] == 0:
                nueva_fila.append('#')
            else:
                nueva_fila.append('.')

        solucion.append(nueva_fila)

    for paso in range(len(camino)):
        fila = camino[paso][0]
        columna = camino[paso][1]

        if paso == 0:
            solucion[fila][columna] = 'I'
        elif paso == len(camino) - 1:
            solucion[fila][columna] = 'F'
        else:
            solucion[fila][columna] = paso

    imprimir_laberinto(solucion)


def main():
    print("LABERINTO ORIGINAL")
    imprimir_laberinto(laberinto)

    if buscar_camino(8, 0, 0):
        print("\n¡El ratón logró salir!")
        print("Puntos mínimos:", PUNTOS_MINIMOS)
        print("Pasos dados:", len(camino) - 1)

        print("\nLABERINTO CON EL CAMINO")
        mostrar_solucion()

        print("\nCamino recorrido:")
        for posicion in camino:
            print(posicion)
    else:
        print("\nEl ratón no logró salir con 23 puntos.")
        print("No se encontró un camino válido.")


main()
