import data_proc
#import hough
import matplotlib.pyplot as plt
import numpy as np
import cv2

#url='D:\\Develop\\SRB\\20120309113756656WHF200T10.0D415data.dat'
url='D:\\Develop\\SRB\\20121113\\0201211130954.dat'
raw = data_proc.load(url)
img = data_proc.normal(raw)
#hough.line(img)


#plt.imshow(img,cmap='gray')
#plt.show()




