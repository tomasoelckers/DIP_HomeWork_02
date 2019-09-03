import numpy as np


def mean(a):
    #  Get the dimensions of a
    (height, width) = a.shape
    # Define sum equal 0
    sum = 0

    # go through the matrix and add every element to sum
    for j in range(height):
        for i in range(width):
            sum += a[j][i]

    # return the mean of a
    return sum / (height * width)


def variance(a):
    # Copy a to new variable
    buff = a.copy()

    #  Get the dimensions of a
    (height, width) = buff.shape

    # Get the mean of a
    m = mean(buff)

    # Define sum equal 0
    sum = 0

    # go through the matrix and add every element with a subtraction of the mean
    for j in range(height):
        for i in range(width):
            # Subtracting mean from the element
            # Squaring the element
            # Adding the element to sum
            sum += (buff[j][i] - m) ** 2

    # return variance
    return sum / (height * width)


# window size 3x3 == 0, 5x5 == 1, 7x7 == 2
def variance_filter(image, size=0):
    # Copy image to new variables
    buff = image.copy()
    temp = image.copy()

    # padding zero in extremes
    buff = (np.pad(buff, pad_width=1, mode='constant', constant_values=0))

    #  Get the dimensions of a
    (height, width) = image.shape

    # go through the matrix and change the pixel value for variance of its 3x3 neighborhood
    for j in range(height):
        for i in range(width):
            if j - 1 - size > 0 and j + 1 + size < height and i - 1 - size > 0 and i + 1 + size < width:
                temp[j][i] = variance(buff[j - 1 - size:j + 2 + size, i - 1 - size:i + 2 + size])

    return temp


def dev_std_filter(image):
    # Copy image to new variables
    buff = image.copy()
    temp = image.copy()

    # padding zero in extremes
    buff = (np.pad(buff, pad_width=1, mode='constant', constant_values=0))

    #  Get the dimensions of a
    (height, width) = image.shape

    # go through the matrix and change the pixel value for variance of its 3x3 neighborhood
    for j in range(height):
        for i in range(width):
            if j - 1 > 0 and j + 1 < height and i - 1 > 0 and i + 1 < width:
                temp[j][i] = np.sqrt(variance(buff[j - 1:j + 2, i - 1:i + 2]))

    return temp


'''x = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16],
              [17, 18, 19, 20]])

print(mean(x), variance(x))
print(np.mean(x), np.var(x))

print(variance_filter(x))'''
