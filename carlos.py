from PIL import Image, ImageFilter

#Introducir la imagen
archivo = input("Introduce la ruta del archivo: ")
imagen = Image.open(archivo)

def rotar():
    #Giramos imagen
    angulo=input("\nIntroduzca el ángulo al que debe rotar su imagen:\n")
    imagen.rotate(angulo)
    imagen.show()

def recortar():
    #Recortamos imagen
    box = (100, 100, 400, 400)
    recortada = imagen.crop(box)
    recortada.show()

def filtros():
    seleccion = input("1=Blur, 2=MinFilter(), 3=MinFilter Selecciona una de las opciones de filtros: ")
    if seleccion==1:
        imagen.filter(ImageFilter.BLUR)
    if seleccion==2:
        imagen.filter(ImageFilter.MinFilter(3))
    if seleccion==3:
        imagen.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
    imagen.show()

def bnw():
    #Convierte la imagen a blanco y negro
    imagen.convert("1")
    imagen.show()

opcion=input("""¿Qué quieres hacer con el archivo?\n
      Si quiere rotar pulse 1, si quiere recortar pulse 2, si ui""")


if opcion==1:
    rotar()
elif opcion==2:
    recortar()
elif opcion==3:
    filtros()
elif opcion==4:
    bnw()