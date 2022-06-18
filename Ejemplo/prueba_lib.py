import cv2
from RC_lib import encontrar_bordes

#Funciona tanto para imagenes en color como en escala de gris
imagen_original=cv2.imread("imagen4.jpg",1)

imagen_original2=cv2.imread("imagen5.JPG",0)

imagen_final,bordes=encontrar_bordes(imagen_original,"binv","ext","rm",5)

imagen_final2,bordes2=encontrar_bordes(imagen_original2,"binv","tree","p",5)

"""
    encontrar_bordes(imagen,tipo_umbral,tipo_contorno,color_borde,ancho_borde)
    ->imagen_bordeada, bordes
    
    Funcion realizada por los alumnos: 
    Cordoba Pablo Ezequiel y Romero Coronado Paul Andrés
    
    Esta funcion encuentra los bordes de una imagen.
    Devuelve la imagen con los bordes dibujados y una matriz con las coordenadas
    de los bordes
    
    imagen: imagen fuente
    tipo_umbral (string): "b" - binaria
                          "binv" - binaria inversa
                          "t" - truncado
                          "tz" - to zero
                          "tzinv" - to zero inversa
                          
    tipo_contorno (string): "ext" - bordes externos
                            "list" - todos los contornos (sin relacion de jerarquia)
                            "ccomp" - contornos externos e internos (huecos)[jerarquia de 2 niveles]
                            "tree" - todos los contornos (con relación de jerarquía)
    
    color_borde (string): "r" - rojo
                          "g" - verde
                          "b" - azul
                          "y" - amarillo
                          "c" - cyan
                          "m" - magenta
                          "o" - naranja
                          "yg" - amarillo_verde
                          "cg" - cyan_verde
                          "cb" - cyan_azul
                          "p" - morado
                          "rm" - rosado/fucsia (rojo_magenta)
						  "k" - negro
    ancho_borde (int): ancho del borde a dibujar
	"""


print("Contorno:",bordes)
cv2.imshow("Imagen original",imagen_original)
cv2.imshow("Imagen original2",imagen_original2)
cv2.imshow("Bordes encontrados",imagen_final)
cv2.imshow("Bordes internos y externos",imagen_final2)
cv2.waitKey()
cv2.destroyAllWindows()
