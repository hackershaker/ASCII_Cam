import cv2 as cv

def setResolution(cam, width, height):
    cam.set(3, width)
    cam.set(4, height)


def openWebcam():
    cap = cv.VideoCapture(0)
    setResolution(cap, 180, 90)

    while(True):
        ret, frame = cap.read()
        frame = cv.resize(frame, (50, 50))
        if(ret) :
            for row in frame[0]:
                for f in row:
                    f = density[-(int(sum(f) / 3) / 255 * 100)-1]
            cv.imshow('camera', frame)
            if cv.waitKey(1) & 0xFF == 27: # esc 키를 누르면 닫음
                print(frame)
                break
        
        
                     
    cap.release()
    cv.destroyAllWindows()
    

if __name__=="__main__":
    density = 'Ñ@#W$9876543210?!abc;:+=-,._ '
    openWebcam()
