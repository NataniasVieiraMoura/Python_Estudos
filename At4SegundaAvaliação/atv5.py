import cv2 as cv
img = cv.imread("WIN_20240930_17_54_51_Pro.jpg")
nova = cv.blur(img, (7,7))
#Aplica a função que suaviza a imagem
cv.imshow("antes", img)
#mostra como era mais limpo
cv.imshow("depois", nova)
#mostra como ficou borrado
cv.waitKey(0)
cv.destroyAllWindows()