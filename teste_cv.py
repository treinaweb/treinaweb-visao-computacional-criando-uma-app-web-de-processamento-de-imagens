import cv2

def brilho_imagem(imagem, resultado):
    img_brilho = cv2.convertScaleAbs(imagem, beta=resultado)
    return img_brilho

def melhora_detalhe(imagem):
    img_melhorada = cv2.detailEnhance(img, sigma_s=34, sigma_r=0.50)
    return img_melhorada

def borra_imagem(imagem, resultado):
    img_borrada = cv2.GaussianBlur(imagem, (7,7), resultado)
    return img_borrada


img = cv2.imread("imagens/DKC2.jpg")

img_processada = brilho_imagem(img, resultado=35)
img_processada = melhora_detalhe(img_processada)
img_processada = borra_imagem(img_processada, resultado=0.5)

cv2.imshow("Imagem Original", img)

cv2.imshow("Imagem Processada", img_processada)

cv2.waitKey(0)

cv2.destroyAllWindows()