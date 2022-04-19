import statistics
import random
import plotly.figure_factory as ff
import csv
import pandas as pd
df=pd.read_csv("StudentsPerformance.csv")
diceresult=df["math score"].to_list()

mean=sum(diceresult)/len(diceresult)
print("mean is ",mean)
median=statistics.median(diceresult)
print("median is ",median)
mode=statistics.mode(diceresult)
print("mode is ",mode)
std_dev=statistics.stdev(diceresult)
print(std_dev)
first_std_dev_start,first_std_dev_end=mean-std_dev,mean+std_dev
second_std_dev_start,second_std_dev_end=mean-(2*std_dev),mean+(2*std_dev)
third_std_dev_start,second_std_dev_end=mean-(3*std_dev),mean+(3*std_dev)

list_of_data_within_1_std_deviation = [result for result in diceresult if result > first_std_dev_start and result < first_std_dev_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(diceresult)))

list_of_data_within_2_std_deviation = [result for result in diceresult if result > second_std_dev_start and result < second_std_dev_end]
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(diceresult)))

list_of_data_within_3_std_deviation = [result for result in diceresult if result > third_std_dev_start and result < second_std_dev_end]
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(diceresult)))

