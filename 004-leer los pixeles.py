from PIL import Image

ruta_imagen = "imagenes/josevicente.jpg"
imagen = Image.open(ruta_imagen)

print(imagen)
anchura,altura = imagen.size
print(anchura,altura)
pixeles = imagen.load()
print(pixeles)
print(pixeles[0,0])