import numpy as np
import plotly.express as px
import pandas as pd
import csv

def data_source(data_path):
    no_of_marks = []
    days_present = []

    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            no_of_marks.append(float(row['Marks']))
            days_present.append(float(row['Days_Present']))

    return {'x':no_of_marks, 'y':days_present}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print(correlation[0,1])

def display():
    data_path = 'one.csv'
    datasource = data_source(data_path)
    find_correlation(datasource)

def scatter():
    df = pd.read_csv('one.csv')
    figure = px.scatter(df, x='Marks', y='Days_Present', color='RollNo')
    figure.show()

display()
scatter()