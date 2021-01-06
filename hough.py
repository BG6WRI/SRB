import cv2
import numpy
import matplotlib.pyplot as plt





img = cv2.imread("burst.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 2.投射到Hough空间进行形状检测
# 任何一条线都可以用(ρ，θ)这两个术语表示。
# 1）先定义一个累加器，(ρ，θ)对应直线，ρ和θ都分别依次增大(根据精度)，计算每对(ρ，θ)的投票数。
#    其中，ρ以像素为单位，θ以弧度为单位。rho和theta是ρ和θ的精度。
# 2）然后，根据threshold(阈值，最低投票数)来判断是否归为一条直线
lines = cv2.HoughLines(edges, 1, numpy.pi / 180, 100)

# 画线
for line in lines:
    rho, theta = line[0]
    a = numpy.cos(theta)
    b = numpy.sin(theta)
    x0 = rho * a
    y0 = rho * b
    # k1*k2=-1 ==> k2=-1/k1
    # k1 = tan(θ) ==> k2 = -1/tan(θ)=-cot(θ)
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    # 画线
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

rho, theta = lines[0][0]

cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyWindow()





import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("burst.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, numpy.pi / 180, 100)




edges = cv2.Canny(gray, 50, 350, apertureSize=3)
cv2.imshow("edges", edges)
cv2.waitKey(0)

#https://blog.csdn.net/wsp_1138886114/article/details/82935839
#gradient
