--------------------------------------edited starts here-----------------------------
import cv2
import numpy as np
from time import sleep

min_width=80 #Minimum rectangle width
height_min=80 #Minimum height of the rectangle

offset=6 #Error allowed between pixel

line_pos=550 #Position of the counting line

delay= 60 #FPS of the video

detect = []
cars = 0


def catch_center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

cap = cv2.VideoCapture('video.mp4')
subtraction = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret , frame1 = cap.read()
    time = float(1/delay)
    sleep(time)
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    img_sub = subtraction.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
    dilated = cv2.morphologyEx (dilated, cv2. MORPH_CLOSE , kernel)
    contour,h=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame1, (25, line_pos), (1200, line_pos), (255.127,0), 3)
    for(i,c) in enumerate(outline):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_contour = (w >= min_width) and (h >= min_height)
        if not validate_outline:
            continues

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        center = handle_center(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0.255), -1)

        for (x,y) in detect:
            if y<(line_pos+offset) and y>(line_pos-offset):
                cars+=1
                cv2.line(frame1, (25, line_pos), (1200, line_pos), (0.127,255), 3)
                detect.remove((x,y))
                print("car is detected : "+str(cars))
    cv2.putText(frame1, "VEHICLE COUNT : "+str(cars), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255,5))
    cv2.imshow("Original Video", frame1)
    cv2.imshow("Detect",dilated)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()

---------------------------------------edited ends here------------------------------


import cv2
import numpy as np
from time import sleep

min_width=80 #Minimum rectangle width
height_min=80 #Minimum height of the rectangle

offset=6 #Error allowed between pixel

pos_linha=550 #Position of the counting line

delay= 60 #FPS of the video

detect = []
cars = 0


def catch_center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

cap = cv2.VideoCapture('video.mp4')
subtraction = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret , frame1 = cap.read()
    time = float(1/delay)
    sleep(time)
    gray = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    img_sub = subtraction.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
    dilated = cv2.morphologyEx (dilated, cv2. MORPH_CLOSE , kernel)
    contour,h=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame1, (25, line_pos), (1200, line_pos), (255.127,0), 3)
    for(i,c) in enumerate(outline):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_contour = (w >= min_width) and (h >= min_height)
        if not validate_outline:
            continues

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        center = handle_center(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0.255), -1)

        for (x,y) in detect:
            if y<(pos_line+offset) and y>(pos_line-offset):
                cars+=1
                cv2.line(frame1, (25, line_pos), (1200, line_pos), (0.127,255), 3)
                detect.remove((x,y))
                print("car is detected : "+str(cars))
    cv2.putText(frame1, "VEHICLE COUNT : "+str(cars), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255,5)
    cv2.imshow("Original Video", frame1)
    cv2.imshow("Detect",dilated)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()

# import cv2
# import numpy as np
# from time import sleep

# largura_min=80 #Largura minima do retangulo
# altura_min=80 #Altura minima do retangulo

# offset=6 #Erro permitido entre pixel  

# pos_linha=550 #Posi????o da linha de contagem 

# delay= 60 #FPS do v??deo

# detec = []
# carros= 0

	
# def pega_centro(x, y, w, h):
#     x1 = int(w / 2)
#     y1 = int(h / 2)
#     cx = x + x1
#     cy = y + y1
#     return cx,cy

# cap = cv2.VideoCapture('video.mp4')
# subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()

# while True:
#     ret , frame1 = cap.read()
#     tempo = float(1/delay)
#     sleep(tempo) 
#     grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(grey,(3,3),5)
#     img_sub = subtracao.apply(blur)
#     dilat = cv2.dilate(img_sub,np.ones((5,5)))
#     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
#     dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
#     dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
#     contorno,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
#     cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (255,127,0), 3) 
#     for(i,c) in enumerate(contorno):
#         (x,y,w,h) = cv2.boundingRect(c)
#         validar_contorno = (w >= largura_min) and (h >= altura_min)
#         if not validar_contorno:
#             continue

#         cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
#         centro = pega_centro(x, y, w, h)
#         detec.append(centro)
#         cv2.circle(frame1, centro, 4, (0, 0,255), -1)

#         for (x,y) in detec:
#             if y<(pos_linha+offset) and y>(pos_linha-offset):
#                 carros+=1
#                 cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0,127,255), 3)  
#                 detec.remove((x,y))
#                 print("car is detected : "+str(carros))        
       
#     cv2.putText(frame1, "VEHICLE COUNT : "+str(carros), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
#     cv2.imshow("Video Original" , frame1)
#     cv2.imshow("Detectar",dilatada)

#     if cv2.waitKey(1) == 27:
#         break
    
# cv2.destroyAllWindows()
# cap.release()

----------------------------ends here------------------------------

import cv2
import numpy as np
from time import sleep

largura_min=80 #Largura minima do retangulo
altura_min=80 #Altura minima do retangulo

offset=6 #Erro permitido entre pixel  

pos_linha=550 #Posi????o da linha de contagem 

delay= 60 #FPS do v??deo

detec = []
carros= 0

	
def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

cap = cv2.VideoCapture('video.mp4')
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret , frame1 = cap.read()
    tempo = float(1/delay)
    sleep(tempo) 
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
    dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    contorno,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (255,127,0), 3) 
    for(i,c) in enumerate(contorno):
        (x,y,w,h) = cv2.boundingRect(c)
        validar_contorno = (w >= largura_min) and (h >= altura_min)
        if not validar_contorno:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 0,255), -1)

        for (x,y) in detec:
            if y<(pos_linha+offset) and y>(pos_linha-offset):
                carros+=1
                cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0,127,255), 3)  
                detec.remove((x,y))
                print("car is detected : "+str(carros))        
       
    cv2.putText(frame1, "VEHICLE COUNT : "+str(carros), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
    cv2.imshow("Video Original" , frame1)
    cv2.imshow("Detectar",dilatada)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
