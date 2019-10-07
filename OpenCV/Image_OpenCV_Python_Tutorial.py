import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# The cv2.line() takes the following parameters: where, start coordinates, end coordinates, color (bgr), line thickness.

# # cv2.rectangle
# void rectangle(Mat& img, Point pt1, Point pt2, const Scalar& color, int thickness=1, int lineType=8, int shift=0)
# 単純な矩形，太線の矩形，塗りつぶされた矩形を描画します．
# # cv2.circle
# void circle(Mat& img, Point center, int radius, const Scalar& color, int thickness=1, int lineType=8, int shift=0)
# 円を描きます．

cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)
cv2.rectangle(img, (15, 25), (200, 150), (0, 0, 255), 15)
cv2.circle(img, (100, 63), 55, (0, 255, 0), -1)

# #np.array(object, dtype=None)
# Create an array.
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# OpenCV documentation had this code, which reshapes the array to a 1 x 2. I did not
# find this necessary, but you may:
# pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (0,130), font, 1, (200, 255, 155), 2, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()