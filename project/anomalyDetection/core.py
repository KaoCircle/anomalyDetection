# -*- coding: utf-8 -*-

from . import testmodule
import csv
from datetime import datetime
import time
# import numpy as np
# import keras
# from keras.layers import *
# from keras.models import Model
# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt
# import syslog


def load_data(file_path):
    print('Load training data.')
    start_time = time.time()

    trip = []
    maxlogi, maxlati = -200, -200
    minlogi, minlati = 200, 200
    with open(file_path, newline='') as csvfile:
        R = csv.DictReader(csvfile)
        for row in R:
            item = []
            item.append(int(row['id'][2:]))  # 0
            item.append(int(row['vendor_id']))  # 1
            item.append(datetime.strptime(row['pickup_datetime'], "%Y-%m-%d %H:%M:%S"))  # 2
            item.append(datetime.strptime(row['dropoff_datetime'], "%Y-%m-%d %H:%M:%S"))  # 3
            item.append(int(row['passenger_count']))  # 4
            item.append(float(row['pickup_longitude']))  # 5
            item.append(float(row['pickup_latitude']))  # 6
            item.append(float(row['dropoff_longitude']))  # 7
            item.append(float(row['dropoff_latitude']))  # 8
            if row['store_and_fwd_flag'] == 'N':
                item.append(bool(0))  # 9
            elif row['store_and_fwd_flag'] == 'Y':
                item.append(bool(1))
            item.append(int(row['trip_duration']))  # 10
            maxlogi = max(item[5], item[7], maxlogi)
            minlogi = min(item[5], item[7], minlogi)
            maxlati = max(item[6], item[8], maxlati)
            minlati = min(item[6], item[8], minlati)
            trip.append(item)

    elapsed_time = time.time() - start_time

    print('Finished loading.', elapsed_time, 'seconds.')
    show_flag()


def show_flag():
    """specify the tags of each item in trip"""
    print('0: id, 1: vendor id, 2: picktime, 3: droptime, 4: passenger count,')
    print('5: pick longitude, 6: pick latitude, 7: drop longitude, 8: drop latitude,')
    print('9: store and fwd flag, 10: duration')


load_data('train.csv')
