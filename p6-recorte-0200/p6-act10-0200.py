import numpy as np
import cv2

# vision artificial Act10 NC 0200
# Lee la imagen en escala de grises
img = cv2.imread("images.webp", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("images.webp 0200", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Linea
print("La linea 0200")
# Crea una imagen negra
img = np.zeros((512, 512, 3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img, (0, 0), (511, 511), (255, 255, 255), 3)

# Abre la ventana con la imagen
cv2.imshow("images.webp 0200", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# El circulo
print("El circulo 0200")
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (256, 256), 10, (255, 0, 0), -1)

# Abre la ventana con la imagen
cv2.imshow("images.webp 0200", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# El texto
print("El texto 0200")
# Añade a la imagen el texto "hola, soy Alejandra" en color blanco
img = cv2.putText(
    img,
    "hola, soy Alejandra",
    (150, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 255),
    2,
)

# Abre la ventana con la imagen
cv2.imshow("images.webp 0200", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# El trackbars
print("El trackbars 0200")


def on_trackbar(val):
    pass


# Crea a una imagen negra, y una ventana llamada 'images 0200'
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("images.webp 0200")

# Crea tres trackbar en la ventana
cv2.createTrackbar("R", "images.webp 0200", 0, 255, on_trackbar)
cv2.createTrackbar("G", "images.webp 0200", 0, 255, on_trackbar)
cv2.createTrackbar("B", "images.webp 0200", 0, 255, on_trackbar)

while True:
    # 1. Muestra la ventana primero
    cv2.imshow("images.webp 0200", img)

    # 2. Revisa las teclas y si la ventana sigue abierta
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or cv2.getWindowProperty("images.webp 0200", cv2.WND_PROP_VISIBLE) < 1:
        break

    # 3. Obtiene las posiciones de los trackbars
    r = cv2.getTrackbarPos("R", "images.webp 0200")
    g = cv2.getTrackbarPos("G", "images.webp 0200")
    b = cv2.getTrackbarPos("B", "images.webp 0200")

    # 4. Actualiza la imagen
    img[:] = [b, g, r]

cv2.destroyAllWindows()

# El thresholding
print("El thresholding 0200")

img = cv2.imread("images.webp", 0)

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("BINARY", thr1)
cv2.imshow("BINARY_INV", thr2)
cv2.imshow("TRUNC", thr3)
cv2.imshow("TOZERO", thr4)
cv2.imshow("TOZERO_INV", thr5)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("programa realizado por Alejandra Rivera NC 0200")