import cv2
import numpy as np
from RC_lib import encontrar_bordes

imagen_original = cv2.imread("imagen4.jpg",1)
imagen_final,bordes=encontrar_bordes(imagen_original,"binv","p",3)

print("Contorno:",bordes)
cv2.imshow("Imagen original",imagen_original)
cv2.imshow("Bordes encontrados",imagen_final)
cv2.waitKey()
cv2.destroyAllWindows()