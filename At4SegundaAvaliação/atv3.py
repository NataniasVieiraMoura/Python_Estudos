import cv2 as cv
img = cv.imread("WIN_20240930_17_54_51_Pro.jpg")
imgdp = cv.resize(img, (200,200),interpolation=cv.INTER_AREA)
#muda a imagem fazendo ela ficar pequena
cv.imshow("antes",img)
#imagem como era
cv.imshow("depois",imgdp)
#imagem de como ficou
cv.waitKey(0)
cv.destroyAllWindows()

'''reduz as imagem e com isso a imagem fica com uma qualidade melhor, logo a imagem
fica com bordas mais definidas'''

