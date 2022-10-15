from hashlib import algorithms_available
import cv2 as cv
from PIL import Image, ImageFont, ImageDraw
import numpy as np

def setResolution(cam, width, height):
    cam.set(3, width)
    cam.set(4, height)

def converttoASCII(frame):
    # print(len(frame))
    # fnt = ImageFont.truetype("arial.ttf", 1)
    # img = Image.new('L', size, color = 'black')
    # draw = ImageDraw.Draw(img)

    # draw.text((0,0), "aaaaaaaaaaaa", fill="white", font=fnt, spacing=0, align="center")
    # img = np.array(img)
    pass

def openWebcam(size=(300, 400)):
    cap = cv.VideoCapture("test.mp4")
    w, h = size
    setResolution(cap, w, h)

    while(True):
        ret, frame = cap.read()
        if(ret):
            
            cv.imshow('camera', frame)
            if cv.waitKey(1) & 0xFF == 27: # esc 키를 누르면 닫음
                # print(frame)
                break
    
    cap.release()
    cv.destroyAllWindows()
    

if __name__=="__main__":
    density = 'Ñ@#W$9876543210?!abc;:+=-,._ '
    size = (200, 100)
    openWebcam(size)
