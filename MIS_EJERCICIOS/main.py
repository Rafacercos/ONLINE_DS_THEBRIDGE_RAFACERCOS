from utils import *
tamaño = pedir_tamaño() 
tablero = crear_tablero(tamaño)    
crear_lista_barcos()
colocar_barcos_random(tablero)
print(tablero)

