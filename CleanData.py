import pandas as pd

"""
Was not letting us submit the huge csv file with the raw dataset on canvas due to it being of such large size. For that reason, we have linked the data set here to its original download location on kaggle where
it can be downloaded and used if you want to see how we cleaned the data using the script.

Here is the link to the dataset: https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018
"""
df = pd.read_csv('allFlights.csv')

df2 = df.drop(columns=['FL_DATE', 'OP_CARRIER_FL_NUM', 'DIVERTED', 'CANCELLED', 'TAXI_OUT', 'CRS_DEP_TIME', 'DEP_TIME', 'WHEELS_OFF', 'WHEELS_ON', 'TAXI_IN', 'CRS_ARR_TIME', 'ARR_TIME', 'CANCELLATION_CODE', 'CRS_ELAPSED_TIME', 'CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'Unnamed: 27'])

df3 = df2.drop(columns=['LATE_AIRCRAFT_DELAY'])
df3.head()

for index, row in df3.iterrows():
    if (row['DEP_DELAY'] < 0):
        row['DEP_DELAY'] = 0


for index, row in df3.iterrows():
    if (row['ARR_DELAY'] < 0):
        row['ARR_DELAY'] = 0

df4 = df3.groupby(['OP_CARRIER', 'ORIGIN', 'DEST'], as_index=False).agg({'DEP_DELAY' : 'mean', 'ARR_DELAY' : 'mean', 'ACTUAL_ELAPSED_TIME': 'mean', 'AIR_TIME': 'mean', 'DISTANCE': 'mean'})

df4.to_csv('FinalFlightDataForProject.csv')