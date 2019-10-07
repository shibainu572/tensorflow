import cv2
import numpy as np

#500 x 250
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

add = img1 + img2
# void add(const Mat& src1, const Mat& src2, Mat& dst)
# 2 つの配列同士，あるいは配列とスカラの 要素毎の和を求めます
add2 = cv2.add(img1, img2)
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

print("add : ", add)
print("cv2.add : ", add2)
print("cv2.addWeighted : ", weighted)

cv2.imshow('add', add)
cv2.imshow('cv2.add', add2)
cv2.imshow('cv2.weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()