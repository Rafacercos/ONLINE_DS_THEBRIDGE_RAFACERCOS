import numpy as np
import random

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, '_')

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Acertaste")
        tablero[casilla] = "X"
    else:
        print("Fallaste")
        tablero[casilla]  = "A"
    return tablero

def crear_barco_aleatorio(eslora):
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    orientacion = random.choice(["Horizontal", "Vertical"])
    if orientacion == "Horizontal":
        columna = random.randint (0,9 - eslora)
        fila = random.randint(0,9)
    elif orientacion == "Vertical" :
        fila = random.randint (0,9 - eslora)
        columna = random.randint(0,9)
    barco_aleatorio = [(fila, columna)]
    while len(barco_aleatorio) < eslora:
        if orientacion == "Horizontal":
            columna = columna + 1
            barco_aleatorio.append((fila, columna))
        else:
            fila = fila + 1
            barco_aleatorio.append((fila, columna))
    return barco_aleatorio

def crear_lista_barcos(lista_esloras=[2,2,2,3,3,4]):
    lista_barcos = []
    for i in lista_esloras:
        lista_barcos.append(crear_barco_aleatorio(i))
    return lista_barcos

def colocar_barcos_random(tablero):
    lista_barcos=crear_lista_barcos()
    for barco in lista_barcos:
        colocar_barco(barco,tablero)
    return(tablero)

def pedir_tamaño():
    while True:
        try:
            filas = int(input("Introduce el numero de filas que deseas para tu tablero (Debe ser un número exacto)"))
            columnas = int(input("Introduce el número de columnas que deseas para tu tablero. (Recuerda que debe ser igual al numero de filas)"))
            tamaño = ((filas),(columnas))
            if filas <= 0 or columnas <= 0:
                print("El número no puede ser 0 o menor, vuelve a introducir los valores")
                continue
            if filas != columnas:
                print("Las filas y columnas deben ser el mismo número. Prueba a introducir los valores otra vez")
                continue
            return tamaño
        except:
             print("Los números deben ser enteros. Prueba a introducirlos otra vez sin decimales")

