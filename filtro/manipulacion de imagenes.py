import cv2
import numpy as np
from PIL import Image

img_path = 'gato.png'
img = cv2.imread(img_path, 0)

imagen_matriz = np.array(Image.fromarray(img))

matriz_final=np.zeros((256,256))

posX=0
posY=0

for i in range(0,256):

    for j in range(0,256):

        aux=0
    
        for x in range(-1,2):
            for y in range(-1,2):
                
                if((x+i)==256 and (y+j)==256):
                    
                    aux=aux+imagen_matriz[0][0]
                    
                elif((y+j)==256):
                    
                    aux=aux+imagen_matriz[i+x][0]
                    
                elif((x+i)==256):
                
                    aux=aux+imagen_matriz[0][j+y]
                    
                else:
            
                    aux=aux+imagen_matriz[i+x][j+y]
                

        aux=aux/9
        
        matriz_final[posX][posY]=aux
        
        posY=posY+1
      
    posX=posX+1
    posY=0
        
array = (matriz_final.astype(np.uint8))

imagen_nueva = Image.fromarray(array)

imagen_nueva.save('nuevoGato.png')

