import numpy as np


def mean(a):
    #  Get the dimensions of a
    (height, width) = a.shape
    # Define sum equal 0
    sum = 0

    # go through the matrix and add every element to sum
    for i in range(height):
        for j in range(height):
            sum += a[i][j]

    # return the mean of a
    return sum / (height * width)


def variance(a):
    #  Get the dimensions of a
    (height, width) = a.shape

    # Get the mean of a
    m = mean(a)

    # Copy a to new variable
    buff = a.copy()

    # Define sum equal 0
    sum = 0

    # go through the matrix and add every element with a subtraction of the mean
    for i in range(height):
        for j in range(width):
            # Subtracting mean from the element
            buff[i][j] -= m

            # Squaring the element
            buff[i][j] *= buff[i][j]

            # Sum the element
            sum += buff[i][j]
    # return variance
    return sum / (height * width)


def variance_filter(image):
    # Copy image to new variable
    buff = image.copy()

    # padding zero in extremes
    buff = (np.pad(buff, pad_width=1, mode='constant', constant_values=0))

    #  Get the dimensions of a
    (height, width) = buff.shape

    for i in range(height):
        for j in range(width):
            if j - 1 > 0 and j + 1 < width and i - 1 > 0 and i + 1 < height:
                buff[i][j] = variance(image)

    pass


x = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print(x)

print(np.mean(x), np.var(x))
print(mean(x), variance(x))

print(x[:][:])
