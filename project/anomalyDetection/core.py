# -*- coding: utf-8 -*-

import dataloader
# import numpy as np
# import keras
# from keras.layers import *
# from keras.models import Model
# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt
# import syslog
DATA_PATH = 'datasets/train.csv'


def helloworld():
    print('hello world')


def main():
    taxi_data = dataloader.load_data(DATA_PATH)
    dataloader.show_flag()
    aj_3d, aj_4d = dataloader.create_am(taxi_data, -74.2, -73.7, 40.5, 40.9, 5, 4)


if __name__ == '__main__':
    main()
