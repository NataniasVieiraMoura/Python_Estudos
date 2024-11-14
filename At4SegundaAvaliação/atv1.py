import cv2 as cv
#Biblioteca
face_classifier = cv.CascadeClassifier("modelo.xml")
#classificador em cascata das imagems
img = cv.imread("WIN_20240930_17_54_51_Pro.jpg")
#lendo imagem no caminho em que ela se emcontra
cinza = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
#transforma a imagem colorida para preto e branco
faces = face_classifier.detectMultiScale(cinza, 1.40,5)
#detecta as bordas da imagem, define a quantidade de processamento e a espeçura da borda
for (x,y,w,h) in faces:#laço que vai marcar a imagem
    cv.rectangle(cinza,(x,y),(x+w,y+h),(225,225,0),3)#formula sobre a imagem, cores da imagem
cv.imshow("depois",cinza)#mostra imagem, define o titulo e a imagem
cv.waitKey(0)#temporizador de app
cv.destroyAllWindows()#finaliza todas as paginas abertas
