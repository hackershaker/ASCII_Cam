import cv2

from filter import Filter


class VideoInput:

    def __init__(self, filter):
        self.filter: Filter = filter

    def run(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            raise RuntimeError("웹캠을 열 수 없습니다.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = self.filter.filter(frame)

            cv2.imshow("WebCam", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
