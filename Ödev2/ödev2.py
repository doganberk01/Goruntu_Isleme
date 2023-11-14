# Gerekli kütüphaneleri içe aktar
import cv2
import numpy as np

# Kamerayı aç
cap = cv2.VideoCapture(0)

# Sonsuz döngü içinde görüntü işleme
while True:
    # Kameradan görüntüyü oku
    _, frame = cap.read()

    # Görüntüyü HSV formatına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı rengin HSV aralığını belirle
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # HSV görüntüsünde kırmızı renge sahip pikselleri maskele
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Maske ile orijinal görüntüyü bitwise_and operatörü ile birleştir
    # Böylece sadece kırmızı nesne görünecek, diğerleri siyah olacak
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Orijinal görüntüyü ekranda göster
    cv2.imshow("Original", frame)

    # Sonucu ekranda göster
    cv2.imshow("Result", result)

    # q tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
cap.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()
