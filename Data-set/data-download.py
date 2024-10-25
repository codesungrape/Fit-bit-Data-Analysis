#import necessary libraries
from pprint import pprint
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

#pull down and print out data in user-friendly format


# Download latest version
file_path = '/Users/shantirai/PycharmProjects/cgf-python/FitBit-data-analysis/Data-set/archive/dailyActivity_merged.csv'
data = pd.read_csv(file_path)
#pprint(data)


def how_many_ids():
    ids = []
    for id in data:
        if id['Id'] not in ids:
            ids.append(id['Id'])
        else:
            ids = ids

    return ids

ids_list = how_many_ids()

