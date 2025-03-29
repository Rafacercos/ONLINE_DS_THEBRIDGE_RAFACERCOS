import os
import shutil
from utils import crear_directorios,cambiar_carpeta,ordenar,doc_types,img_types,software_types
carpeta = "downloads"
cambiar_carpeta(carpeta)
crear_directorios()
ordenar()
print("He terminado de ordenar")