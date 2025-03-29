import os
import shutil

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')


def cambiar_carpeta(carpeta):
    os.chdir(f"C:/Users/rafac/{carpeta}")
    return os.getcwd()

def crear_directorios():
    os.mkdir("Documentos")
    os.mkdir("Imagenes")
    os.mkdir("Software")
    os.mkdir("Otros")

def ordenar():
    for archivo in os.listdir():
        if '.' not in archivo:
            continue
        elif os.path.splitext(archivo)[1] in doc_types:
            destino = f"./Documentos/{archivo}"
            shutil.move (archivo,destino)
        elif os.path.splitext(archivo)[1] in img_types:
            destino = f"./Imagenes/{archivo}"
            shutil.move (archivo,destino)
        elif os.path.splitext(archivo)[1] in software_types:
            destino = f"./Software/{archivo}"
            shutil.move (archivo,destino)
        else:
            destino = f"./Otros/{archivo}"
            shutil.move (archivo,destino)
    return os.listdir()