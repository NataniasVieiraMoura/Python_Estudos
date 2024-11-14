import cv2 as cv
#biblioteca
img = cv.imread("WIN_20240930_17_54_51_Pro.jpg")
cv.imshow("antes",img)
#tabela antes da mudança
mudado = cv.Canny(img,100,70)
#Dimensionamento de imagem para detecção de bordas
cv.imshow("depois",mudado)
#tabela depois da mundança
cv.waitKey(0)
cv.destroyAllWindows()