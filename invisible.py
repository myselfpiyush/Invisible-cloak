import cv2
import numpy as np

cap = cv2.VideoCapture(0)

back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)
        # how to get hsv value
        # lower:hue-10,100,100 and higher: hue+10,255,255
        red = np.uint8([[[0, 0, 255]]])  # bgr value of red
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)  # get hsv value of red from bgr

        # threshold the hsv value to get only the red colors
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)


        part_1 = cv2.bitwise_and(back, back, mask=mask)

        mask=cv2.bitwise_not(mask)

        part_2 = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("result", part_1+part_2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()