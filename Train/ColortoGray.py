import cv2

video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BRG2GRAY)
        cv2.imshow("image", frame)
    if cv2.waitKey() == ord('q'):
        break

# stop using camera
video.release()
cv2.destroyAllWindows()
