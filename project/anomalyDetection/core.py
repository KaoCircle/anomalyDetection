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
    dataloader.load_data(DATA_PATH)
    dataloader.show_flag()


if __name__ == '__main__':
    main()
