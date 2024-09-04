import cv2

video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    cv2.imshow('Test Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
