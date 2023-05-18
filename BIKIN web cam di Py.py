import cv2
import time

pedo = cv2.VideoCapture(0)

while True:
    _, frame = pedo.read()
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

pedo.release()
cv2.destroyAllWindows()
