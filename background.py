import cv2
# this is my webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()  # here i am simply reading from webcam
    # back :- is what the camera is reading or print what are you getting
    # ret :- it is what are you reading is successful or not
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):  # after 5 sec it will going to take a picture
            # save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()