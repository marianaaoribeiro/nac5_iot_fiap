import cv2
import os,sys, os.path
import numpy as np
import math
import argparse


parser = argparse.ArgumentParser(description="Filtros HSV (lower) + (upper)")
parser.add_argument("-l1","-lower1",type=str,help="Filtros HSV lower (Baixo), separe por virgulas\nEX: 255,255,255")
parser.add_argument("-l2","-lower2",type=str,help="Filtros HSV lower (Baixo), separe por virgulas\nEX: 255,255,255")

parser.add_argument("-u1","-upper1",type=str,help="Filtros HSV upper (Alto), separe por virgulas\nEX: 255,255,255")
parser.add_argument("-u2","-upper2",type=str,help="Filtros HSV upper (Alto), separe por virgulas\nEX: 255,255,255")

args = parser.parse_args()
lower1 = args.l1
lower1 = lower1.split(",")
lower1 = [float(i) for i in lower1]

lower2 = args.l2
lower2 = lower2.split(",")
lower2 = [float(i) for i in lower2]

upper1 = args.u1
upper1 = upper1.split(",")
upper1 = [float(i) for i in upper1]

upper2 = args.u2
upper2 = upper2.split(",")
upper2 = [float(i) for i in upper2]



#filtro baixo
image_lower_hsv1 = np.array(lower1)
image_upper_hsv1 = np.array(upper1)
#filtro alto
image_lower_hsv2 = np.array(lower2)
image_upper_hsv2 = np.array(upper2)


def filtro_de_cor(img_bgr, low_hsv, high_hsv):
    """ retorna a imagem filtrada"""
    img = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, low_hsv, high_hsv)
    return mask 

def mascara_or(mask1, mask2):

    """ retorna a mascara or"""
    mask = cv2.bitwise_or(mask1, mask2)
    return mask

def mascara_and(mask1, mask2):
     """ retorna a mascara and"""
     mask = cv2.bitwise_and(mask1, mask2)
     
     return mask

def desenha_cruz(img, cX,cY, size, color):
     """ faz a cruz no ponto cx cy"""
     cv2.line(img,(cX - size,cY),(cX + size,cY),color,5)
     cv2.line(img,(cX,cY - size),(cX, cY + size),color,5)    

def escreve_texto(img, text, origem, color):
     """ faz a cruz no ponto cx cy"""
 
     font = cv2.FONT_HERSHEY_SIMPLEX
     cv2.putText(img, str(text), origem, font,1,color,2,cv2.LINE_AA)

def image_da_webcam(img):
    """
    ->>> !!!! FECHE A JANELA COM A TECLA ESC !!!! <<<<-
        deve receber a imagem da camera e retornar uma imagems filtrada.
    """  
    mask_hsv1 = filtro_de_cor(img, image_lower_hsv1, image_upper_hsv1)
    mask_hsv2 = filtro_de_cor(img, image_lower_hsv2, image_upper_hsv2)
    
    mask_hsv = mascara_or(mask_hsv1, mask_hsv2)
    
    mask_hsv = filtro_de_cor(img, image_lower_hsv1, image_upper_hsv1)
    
    contornos, _ = cv2.findContours(mask_hsv, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    mask_rgb = cv2.cvtColor(mask_hsv, cv2.COLOR_GRAY2RGB) 
    contornos_img = mask_rgb.copy()
    
    data = {}

    for c in contornos:
        area = cv2.contourArea(c)
        if not len(data) <= 1:
            if area > max(list(data.keys())):  
                data[min(list(data.keys()))] = c
                data[area] = data.pop(min(list(data.keys())))

        else: data[area] = c
    
    pos = 0
    centros = []
    for area in list(data.keys()):
        pos += 50
            
        M = cv2.moments(data[area])
        # Verifica se existe alguma para calcular, se sim calcula e exibe no display
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            cv2.drawContours(contornos_img, [data[area]], -1, [255, 0, 0], 5)
        
            #faz a cruz no centro de massa
            desenha_cruz(contornos_img, cX,cY, 20, (0,0,255))
            centros.append((cX,cY))
            
            # Para escrever vamos definir uma fonte 
            texto = area
            origem = (cX-90,cY-50)
            escreve_texto(contornos_img, texto, origem, (0,255,0)) 
                
        else:
        # se não existe nada para segmentar
            cX, cY = 0, 0
            # Para escrever vamos definir uma fonte 
            texto = 'nao tem nada'
            origem = (0,50)
            escreve_texto(contornos_img, texto, origem, (0,0,255))
    try:
        cv2.line(contornos_img, centros[0], centros[1], (0,255,0), 5)
        xangulo = centros[0][0] - centros[1][0]
        yangulo = centros[0][1] - centros[1][1]
        angulo = int(round(math.degrees(math.atan2(xangulo,yangulo)),0))
        cv2.putText(contornos_img, "Angulo: " +str(angulo),(450,50), cv2.FONT_HERSHEY_TRIPLEX,1,(0,255,0),2,cv2.LINE_AA)    
    except: pass
    
    return contornos_img

cv2.namedWindow("preview")
# define a entrada de video para webcam
vc = cv2.VideoCapture(0)

#vc = cv2.VideoCapture("video.mp4") # para ler um video mp4 

#configura o tamanho da janela 
vc.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    
    img = image_da_webcam(frame) # passa o frame para a função imagem_da_webcam e recebe em img imagem tratada



    cv2.imshow("preview", img)
    cv2.imshow("original", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()
