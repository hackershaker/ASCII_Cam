from unittest import TestCase, main
import cv2 as cv
import ascii_filter

class testclass(TestCase):
    def testconvert(self):
        img = cv.imread("test.jpg", cv.IMREAD_COLOR)
        result = ascii_filter.converttoASCII(img)
        cv.imwrite('testresult.jpg', result)


if __name__=="__main__":
    main()