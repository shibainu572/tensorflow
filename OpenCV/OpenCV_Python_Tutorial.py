import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
# ピクセルのレファランスを定義します。
px = img[55, 55]

# 次に、実際にピクセルを変更します。
img[55, 55] = [255, 255, 255]

# その後、 再定義します。
px = img[55, 55]
print(px)

# ROIまたは画像の領域を定義できます。
# ROI（Region of Interest）とは、画像データのうち、操作の対象として選ぶ領域のことです。
# 「対象領域」「注目領域」「関心領域」などともいいます。
px = img[100:150, 100:150]
print(px)

# ROIを修正する。
img[100:150, 100:150] = [255, 255, 255]

print(img.shape)
print(img.size)
print(img.dtype)

watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()