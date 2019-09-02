import cv2
import matplotlib.pyplot as plt

# Direction path and name of the picture file.
DIR = 'Images/'
Image = 'leaf.png'

# Load image
im = cv2.imread(DIR+Image, 0)

# Get the shape of the picture
(Height, Width) = im.shape[:2]

# Display picture
plt.figure(1)
plt.imshow(im, cmap='gray')
plt.show()

# Display the result of the Where is Waldo? problem
'''cv2.namedWindow('Picture', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Picture', 800, 600)
cv2.imshow('Picture', im)
cv2.waitKey(0)
cv2.destroyAllWindows()'''