import numpy as np
import plotly.express as px
import pandas as pd
import csv

def data_source(data_path):
    coffee = []
    sleep = []

    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row['Coffee']))
            sleep.append(float(row['Sleep']))

    return {'x':coffee, 'y':sleep}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print(correlation[0,1])

def display():
    data_path = 'two.csv'
    datasource = data_source(data_path)
    find_correlation(datasource)

def scatter():
    df = pd.read_csv('two.csv')
    figure = px.scatter(df, x='Coffee', y='Sleep', color='Week')
    figure.show()

display()
scatter()