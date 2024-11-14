'''Atividade 4: Detecção de bordas com Canny'''
import cv2 as cv#biblioteca
img = cv.imread("archive/data/lena.jpg")#importação de imagem
cv.imshow("Imagem original",img)#tabela com imagem original
edges = cv.Canny(img,100,70)#Dimensionamento de imagem para detecção de bordas
cv.imshow("Imagem alterada",edges)#tabela com imagem alterada
cv.waitKey(0)#tempo de espera da aba criada
cv.destroyAllWindows()#fechar todas as abas existentes após fim do programa