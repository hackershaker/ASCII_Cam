from hashlib import algorithms_available
from lib2to3.pytree import convert
import cv2 as cv
from PIL import Image, ImageFont, ImageDraw
import numpy as np

density = 'Ñ@#W$9876543210?!abc;:+=-,._ '
asciiresolution = (50,50)
fontsize = 10

def setResolution(cam, width, height):
    cam.set(3, width)
    cam.set(4, height)

def converttoASCII(frame, size=asciiresolution):
    frame = cv.resize(frame, size)
    cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # print(len(frame), len(frame[0]))
    fnt = ImageFont.truetype("arial.ttf", fontsize)
    img = Image.new('L', (size[0]*fontsize, size[1]*fontsize), color = 'black')
    draw = ImageDraw.Draw(img)

    for i in range(size[0]):
        for j in range(size[1]):
            light = density[int(sum(frame[i][j])/(256*3) * len(density))]
            draw.text((j*fontsize, i*fontsize), light, fill="white", font=fnt, spacing=0, align="center")

    img = np.array(img)
    return img

def openWebcam(size=(300, 400), source=0):
    cap = cv.VideoCapture(source)
    w, h = size
    setResolution(cap, w, h)

    while(True):
        ret, frame = cap.read()
        if(ret):
            frame = converttoASCII(frame)
            cv.imshow('camera', frame)
            if cv.waitKey(1) & 0xFF == 27: # esc 키를 누르면 닫음
                # print(frame)
                break
    
    cap.release()
    cv.destroyAllWindows()
    

if __name__=="__main__":
    openWebcam()
