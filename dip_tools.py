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
    # Copy a to new variable
    buff = a.copy()

    #  Get the dimensions of a
    (height, width) = buff.shape

    # Get the mean of a
    m = mean(buff)

    # Define sum equal 0
    sum = 0

    # go through the matrix and add every element with a subtraction of the mean
    for i in range(height):
        for j in range(width):
            # Subtracting mean from the element
            # Squaring the element
            # Adding the element to sum
            sum += (buff[i][j] - m) ** 2

    # return variance
    return sum / (height * width)


def variance_filter(image):
    # Copy image to new variable
    buff = image.copy()

    # padding zero in extremes
    buff = (np.pad(buff, pad_width=1, mode='constant', constant_values=0))
    temp = buff.copy()

    #  Get the dimensions of a
    (height, width) = buff.shape

    for i in range(height):
        for j in range(width):
            if j - 1 > 0 and j + 1 < width and i - 1 > 0 and i + 1 < height:
                temp[i][j] = variance(buff[j - 1:j + 2, i - 1:i + 2])

    # Delete the extremes rows
    result = temp[~np.all(temp == 0, axis=1)]
    # Delete the extremes columns
    result = np.delete(result, np.s_[::width - 1], 1)

    return result


'''x = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print(np.var(x), variance(x))

i, j = 2, 1
print(x[j - 1:j + 2, i - 1:i + 2])'''
