#import library
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimage
import os
#membaca citra digital dari folder yang ada di komputer
citra = cv2.imread("D:\Semester 4_Henny\Pencitraan Digital\PRAKTIKUM PCD\sunflower.jpg")
#menampilkan citra digital yang sudah dibaca
cv2.imshow("sunflower", citra)
#menampilkan matriks dari citra
#menampilkan semua channel warna dalam citra
print(citra)
#menampilkan channel warna blue
print(citra[:,:,0])
#menampilkan channel warna green
print(citra[:,:,1])
#menampilkan channel warna red
print(citra[:,:,2])
#menunggu sampai user sembarang tombol baru akan close
cv2.waitKey()

x = [24, 25, 26]
y = [23, 24, 25]

plt.plot(x,y)
plt.show()