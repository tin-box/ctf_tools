import cv2              #pip install opencv-python
import numpy as np      #pip install numpy
import matplotlib.pyplot as plt
import sys

xor_img = cv2.bitwise_xor(cv2.imread(sys.argv[1]),cv2.imread(sys.argv[2]))    # bitwise XOR on images
plus_img = ((cv2.imread(sys.argv[1]) + cv2.imread(sys.argv[2])))
minus_img = ((cv2.imread(sys.argv[1]) - cv2.imread(sys.argv[2])))
plt.subplot(131), plt.imshow(xor_img), plt.title("XOR")
plt.subplot(132), plt.imshow(plus_img), plt.title("PLUS")
plt.subplot(133), plt.imshow(minus_img), plt.title("MINUS")
plt.show()