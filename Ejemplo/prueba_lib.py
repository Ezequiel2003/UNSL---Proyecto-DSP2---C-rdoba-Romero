import cv2
from RC_lib import encontrar_bordes

#Funciona tanto para imagenes en color como en escala de gris
imagen_original=cv2.imread("imagen4.jpg",1)

imagen_original2=cv2.imread("imagen5.JPG",0)


imagen_final,bordes=encontrar_bordes(imagen_original,"binv","ext","rm",5)

imagen_final2,bordes2=encontrar_bordes(imagen_original2,"binv","tree","p",5)


print("Contorno:",bordes)
cv2.imshow("Imagen original",imagen_original)
cv2.imshow("Imagen original2",imagen_original2)
cv2.imshow("Bordes encontrados",imagen_final)
cv2.imshow("Bordes internos y externos",imagen_final2)
cv2.waitKey()
cv2.destroyAllWindows()
