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
    return print (tablero)