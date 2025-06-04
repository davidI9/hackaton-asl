from PIL import Image, ImageFilter, ImageDraw
import requests, io

opt = int(input("Introduce si quieres url (1) o archivo local (2):\n"))

if opt == 1:
    archivo = input("Introduzca la url:\n")
    response = requests.get(archivo, stream=True)
    imagen = Image.open(io.BytesIO(response.content))
elif opt == 2:
    archivo = input("Introduce la ruta del archivo:\n")
    imagen = Image.open(archivo)

def rotar():
    #Giramos imagen
    angulo=input("\nIntroduzca el ángulo al que debe rotar su imagen:\n")
    imagen.rotate(int(angulo)).show()

def recortar():
    #Recortamos imagen
    width, height = imagen.size
    print(f"El ancho son {width} pixeles d ancho y {height} pixeles de alto")
    a=input("Recortar por la izquierda (pixels):\n")
    b=input("Recortar por arriba (pixels):\n")
    c=input("Recortar por la derecha (pixels):\n")
    d=input("Recortar por abajo (pixels):\n")
    box = (int(a), int(b), int(c), int(d))
    imagen.crop(box).show()

def filtros():
    #Añadimos filtros a la i
    seleccion = int(input("1=Blur, 2=Contour, 3=Detail 4=Find_Edges 5=Emboss \nSelecciona una de las opciones de filtros:\n"))
    if (seleccion==1):
        imagen.filter(ImageFilter.BLUR).show()
    elif (seleccion==2):
        imagen.filter(ImageFilter.CONTOUR).show()
    elif (seleccion==3):
        imagen.filter(ImageFilter.DETAIL).show()    
    elif (seleccion==4):
        imagen.filter(ImageFilter.FIND_EDGES).show()
    elif (seleccion==5):
        imagen.filter(ImageFilter.EMBOSS).show()
    

def bnw():
    #Convierte la imagen a monocromático
    imagen.convert("L").show()

def cooler_bnw():
    #Convierte la imagen a blanco y negro
    image=imagen.convert("L")
    image.convert("1").show()
    
def jonkler():
    #Jonkler
    joker=Image.open("imagen/jonkler.jpg")
    joker.show()

while True:
    print("Menú principal:")
    print("1. Girar")
    print("2. Recortar")
    print("3. Filtros")
    print("4. Blanco y Negro")
    print("5. Blanco y Negro pero épico")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion=="1":
        rotar()
    elif opcion == "2":
       recortar()
    elif opcion == "3":
       filtros()
    elif opcion == "4":
       bnw()
    elif opcion == "5":
        cooler_bnw()
    elif opcion == "33":
        jonkler()
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida")