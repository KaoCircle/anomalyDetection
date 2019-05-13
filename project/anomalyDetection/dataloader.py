import csv
from datetime import datetime
import time
import numpy as np


def load_data(file_path):
    print('Load training data... usually takes 1 minute')
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
            item.append(
                datetime.strptime(row['pickup_datetime'],
                                  "%Y-%m-%d %H:%M:%S"))  # 2
            item.append(
                datetime.strptime(row['dropoff_datetime'],
                                  "%Y-%m-%d %H:%M:%S"))  # 3
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
    print('longitude:', minlogi, 'to', maxlogi, ', latitude:', minlati, 'to', maxlati)
    return trip


def show_flag():
    """specify the flag of each item in trip"""
    print('0: id, 1: vendor id, 2: picktime, 3: droptime, 4: passenger count,')
    print('5: pick longitude, 6: pick latitude, 7: drop longitude,')
    print('8: drop latitude, 9: store and fwd flag, 10: duration')


def show_range():
    """specify the range of time and space"""
    print('According to the data provider:')
    print('longitude range: -61 to -122, latitude range: 52-32')
    print('time range: 2016-01-01 to 2016-07-01')


def create_am(trip, minlogi, maxlogi, minlati, maxlati, x_block, y_block):
    print('Generating adjacency matrice...')
    start_time = time.time()
    mintime = datetime.strptime('2016-1-1 0:0:0', "%Y-%m-%d %H:%M:%S")
    logi_len = (maxlogi-minlogi)/x_block
    lati_len = (maxlati-minlati)/y_block
    n_block = x_block*y_block
    n_input = (n_block+1) ** 2

    def which_block(x, y):
        '''return 0-19 for points inside boundary, 20 for otherwise'''
        if (x > minlogi) and (x < maxlogi) and (y > minlati) and (y < maxlati):
            x = int((x-minlogi)/logi_len)
            y = int((y-minlati)/lati_len)
            return y*x_block+x
        else:
            return n_block

    # adjacency matrice, 26*7*441
    # 26 weeks, 7 days
    # there are 20+1 blocks in the map
    # each people traveling is counted in 21*21=441 array
    aj = np.zeros((26, 7, n_input))
    for t in trip:
        orig = which_block(t[5], t[6])
        dest = which_block(t[7], t[8])
        date = (t[2]-mintime).days
        week, weekday = divmod(date, 7)
        if week < 26:
            aj[week][weekday][orig+dest*n_block] += t[4]

    elapsed_time = time.time() - start_time
    print('Finished generating.', elapsed_time, 'seconds.')
    return aj
