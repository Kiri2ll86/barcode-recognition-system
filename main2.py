import cv2
import os
from pyzbar.pyzbar import decode

# Мой RTSP URL для настройки OpenCV
RTSP_URL = 'rtsp://admin:admin@192.168.0.104:1935/h264Preview_01_main'
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Обнаружение и декодирование штрих-кодов
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        print('Data:', obj.data)
        cv2.putText(frame, str(obj.data), (obj.rect.left, obj.rect.top), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.rectangle(frame, (obj.rect.left, obj.rect.top), (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height), (0, 255, 0), 2)

    # Отображение кадра со штрих-кодами
    cv2.imshow('RTSP stream with barcodes', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
