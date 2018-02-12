import pandas as pd
import numpy as n
import sys

list_ = []
for file_ in sys.argv[1:]:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)

frame = pd.concat(list_)
frame.to_csv("combined.csv")

#Read CSV
csv_data1 = pd.read_csv('data1.csv')

#Get columns information
columns = csv_data1.columns.tolist()


#Calculate average for each column
column_average = {}
for column in columns:
    if column == 'TIME':
        continue
    column_values = csv_data1.get(column).tolist()

    # Find percentile value - Lets say 70% and filter data based on the percentile value
    temp_array = n.array(column_values)
    try:
        percentile_value = n.percentile(temp_array,70)
        column_values_more = [x for x in column_values if x >= percentile_value]
        column_values_less = [x for x in column_values if x <= percentile_value]
        if len(column_values_more) > len(column_values_less):
            column_values = column_values_more
        else:
            column_values = column_values_less
        average = sum(column_values)/len(column_values)
    except TypeError,e:
        average = 'NA'
    except ZeroDivisionError,e:
        average = 'ZE'
    column_average[column] = average


def benchmark_generator(value_list):
    pass


#Predict benchmark value
for column in columns:
    benchmark_value = csv_data1.apply(benchmark_generator,axis=0)

print column_average

#We then build benchmark file using the above dictionary.
