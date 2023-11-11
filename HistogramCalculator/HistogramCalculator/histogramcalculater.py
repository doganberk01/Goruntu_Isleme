import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntü yolunu belirtin (raw string olarak)
image_path = "ornek_goruntu.png"

# Gri seviye görüntüyü yükle
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Histogramı hesaplamak için bir dizi oluştur
histogram = np.zeros(256, dtype=int)

# Görüntü üzerinde dolaşarak histogramı hesapla
for row in image:
    for pixel_value in row:
        histogram[pixel_value] += 1

# Histogramı görselleştir
plt.bar(range(256), histogram, width=1.0, color='b')
plt.title('Gri Seviye Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()
