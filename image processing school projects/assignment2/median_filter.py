import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy
from PIL import Image


def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final


def main():
    img = Image.open("CSE467.png").convert(
        "Median")
    arr = numpy.array(img)
    removed_noise = median_filter(arr, 11)
    img = Image.fromarray(removed_noise)
    img.show()


main()
#median = cv2.medianBlur(img,5)


#plt.subplot(121),plt.imshow(img),plt.title('Original')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(blur),plt.title('Median Filter')
#plt.xticks([]), plt.yticks([])
#plt.show()
