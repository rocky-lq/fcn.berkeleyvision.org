import matplotlib
matplotlib.use('TkAgg')
# print(matplotlib.get_backend())
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
import os

source_list = [[],[],[]]


title_list = np.array(['origin','FCN-8s', 'Deeplab'])

for files in os.listdir('segmentation/Image'):
    source_list[0].append('segmentation/Image/'+files)

for files in os.listdir('segmentation/Prediction'):
    source_list[1].append('segmentation/Prediction/'+files)

for files in os.listdir('segmentation/deeplab'):
    source_list[2].append('segmentation/deeplab/'+files)

limit = 5

def show_image(source_list, title_list):
    x = 5
    y = 3
    for i in range(x):
        for j in range(y):
            plt.subplot(x, y, i * y + j + 1)
            plt.axis('off')
            if i == 0:
                plt.title(title_list[j])
            plt.imshow(image.imread(source_list[j][i]))

    # plt.show()

show_image(source_list, title_list)


# print('end')
