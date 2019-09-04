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

# im_filtered = dip_tools.std_dev_filter(im)
im_filtered = dip_tools.variance_filter(im, dof=1)

# Work with Sobel and Laplacian filters: ksize = kernel size.

# cv2 Sobel filter.
# im_filtered = cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize=3) # sobel x
# im_filtered = cv2.Sobel(im, cv2.CV_64F, 0, 1, ksize=3) # sobel y
# im_filtered = cv2.Sobel(im, cv2.CV_64F, 1, 1, ksize=7) # sobel

# cv2 Laplacian filter.
# im_filtered = cv2.Laplacian(im, cv2.CV_64F, ksize=7)

# cv2 Canny Edge Detection
# im_filtered = cv2.Canny(im, 100, 100)
pass

# Display picture
plt.figure(1)
plt.imshow(im, cmap='gray')
plt.show()

# Display filtered picture
plt.figure(2)
plt.imshow(im_filtered, cmap='gray')
plt.show()

# Save picture filtered
cv2.imwrite('Images_Results/variance/' + 'leaf_var_filtered_3x3_ddof_1.png', im_filtered)
