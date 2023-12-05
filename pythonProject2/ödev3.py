import cv2

# Görüntüyü oku
img = cv2.imread("image.jpg")

# Görüntüyü grayscale olarak dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüyü ikili olarak dönüştür
# Eşik değeri olarak 127 seç
# Eşik değerinden küçük olan pikseller 0 (siyah), büyük olanlar 255 (beyaz) olur
thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

# Görüntüdeki beyaz nesnelerin sayısını bul
# Etiketleme algoritmasını uygula
# Her beyaz nesneye bir etiket atayacak şekilde görüntüyü tarayacak
# Etiket sayısı, pirinç tanelerinin sayısına eşittir
num_labels, labels = cv2.connectedComponents(thresh)

# Pirinç tanelerinin sayısını ekrana yazdır
# Etiket sayısından 1 çıkar, çünkü arka plan da bir etiket olarak sayılır
print(f"Görüntüdeki pirinç tanelerinin sayısı: {num_labels - 1}")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB)

# Görüntülerin boyutunu değiştir
# Görüntülerin boyutunu 500x500 piksel olarak ayarla
img = cv2.resize(img, (500, 500))
thresh = cv2.resize(thresh, (500, 500))

cv2.imshow("Original Image", img)
cv2.imshow("Processed Image", thresh)

cv2.waitKey(0)

cv2.destroyAllWindows()
