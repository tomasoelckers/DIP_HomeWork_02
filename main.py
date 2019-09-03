import cv2
import matplotlib.pyplot as plt
import dip_tools

# Direction path and name of the picture file.
DIR = 'Images/'

Image = 'leaf.png'  # leaf 256 x 255
# Image = 'bacteria.jpg'  # bacteria 1836 x 3264

# Load image
# Load image
im = cv2.imread(DIR + Image, 0)

# Get the shape of the picture
(Height, Width) = im.shape[:2]

# Work with variance and standard deviation filters

im_filtered = dip_tools.std_dev_filter(im)
# im_filtered = dip_tools.variance_filter(im, 1)

# Work with Sobel and Laplacian filters: ksize = kernel size.

# cv2 Sobel filter.
# im_filtered = cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize=5)
# im_filtered = cv2.Sobel(im, cv2.CV_64F, 0, 1, ksize=5)
# im_filtered = cv2.Sobel(im, cv2.CV_64F, 1, 1, ksize=5)

# cv2 Laplacian filter.
# im_filtered = cv2.Laplacian(im, cv2.CV_64F, ksize=5)


# Display picture
plt.figure(1)
plt.imshow(im, cmap='gray')
plt.show()

# Display filtered picture
plt.figure(2)
plt.imshow(im_filtered, cmap='gray')
plt.show()

# Save picture filtered
cv2.imwrite('Images_Results/variance/'+'leaf_std_dev_filtered_3x3.jpg', im_filtered)

# Display the result on CV2
'''cv2.namedWindow('Picture', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Picture', 800, 600)
cv2.imshow('Picture', im)
cv2.waitKey(0)
cv2.destroyAllWindows()'''