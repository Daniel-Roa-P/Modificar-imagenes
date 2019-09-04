import cv2
import numpy as np
from PIL import Image
import random

img_path = 'pikachu.png'
img = cv2.imread(img_path, 0)

imagen_matriz = np.array(Image.fromarray(img))
        
valores = np.arange(16)
imagen_nueva = np.full((256,256),0)

for x in range(0,4):
    
    for y in range(0,4):
        
        i=random.randint(0,len(valores)-1)
        
        posX= int(valores[i]/4)
        posY= valores[i] % 4
        
        imagen_nueva[64*(x):64*(x+1),64*(y):64*(y+1)]=imagen_matriz[64*(posX):64*(posX+1),64*(posY):64*(posY+1)];
        
        valores = np.delete(valores, i)
        

imagen_matriz[0:64,0:64]=imagen_matriz[64:128,64:128]

array = (imagen_nueva.astype(np.uint8))

imagen_nueva = Image.fromarray(array)

imagen_nueva.save('nuevoPikachu.png')