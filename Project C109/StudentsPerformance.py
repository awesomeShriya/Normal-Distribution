import statistics
import pandas as pd
import plotly.graph_objects as go
import csv
import random
import plotly.figure_factory as ff

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()
mean=sum(data)/len(data)
median=statistics.median(data)
mode=statistics.mode(data)
std_deviation=statistics.stdev(data)

first_std_start,first_std_end=mean-std_deviation,mean+std_deviation
second_std_start,second_std_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_start,third_std_end=mean-(3*std_deviation),mean+(3*std_deviation)

list_data_1_stdev=[result for result in data if result>first_std_start and result<first_std_end]
list_data_2_stdev=[result for result in data if result>second_std_start and result<second_std_end]
list_data_3_stdev=[result for result in data if result>third_std_start and result<third_std_end]

print("mean of the data is{}".format(mean))
print("median of the data is{}".format(median))
print("mode of the data is{}".format(mode))
print("standard deviation of the data is{}".format(std_deviation))

print("{}% of data lies within 1st standard deviation".format(len(list_data_1_stdev)*100.0/len(data)))
print("{}% of data lies within 2nd standard deviation".format(len(list_data_2_stdev)*100.0/len(data)))
print("{}% of data lies within 3rd standard deviation".format(len(list_data_3_stdev)*100.0/len(data)))