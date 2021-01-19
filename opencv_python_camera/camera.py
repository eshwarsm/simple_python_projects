import cv2
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame = camera.read()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Python Camera',frame)
