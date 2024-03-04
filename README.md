# barcode-recognition-system
Сделана система распознавания штрих кодов, с помощью библиотеки видеообработки opencv. Для захвата изображения будем использовать Ваш смартфон, который необходимо будет по wi-fi подключить к ПК, и организовать трансляцию по rtsp потоку, сделать это (для примера) можно с помощью Free Security Camera. Далее передаем поток на ПК, проверяем его захват. Далее можно воспользоваться библиотекой для чтения штрих кодов. После прочтения штрих кода, необходимо будет через сайт https://barcode-list.ru/barcode/RU/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA.htm?barcode=6921734941299, определить товар.
#
+ Для захвата изображения
import cv2
import os
from pyzbar.pyzbar import decode
Мой RTSP URL и настройки OpenCV
RTSP_URL = 'rtsp://admin:admin@192.168.0.104:1935/h264Preview_01_main'
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

Создание объекта VideoCapture
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
cap.release()
cv2.destroyAllWindows() 
## Результат
![Image alt](https://i.postimg.cc/FR8YzrDd/1.png)
+ для разработки алгоритма проверки текста - https://pythonim.ru/osnovy/regulyarnye-vyrazheniya-python, https://python2030.ru/
## Результат
![Image alt](https://i.postimg.cc/FR8YzrDd/1.png)
