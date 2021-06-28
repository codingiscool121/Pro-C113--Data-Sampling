import statistics as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.figure_factory as pf
data = pd.read_csv("savings_data_final.csv")
read=data["quant_saved"]

plot = sns.boxplot(data=data, x=data["quant_saved"])

q1= data["quant_saved"].quantile(0.25)
q3 = data["quant_saved"].quantile(0.75)
iqr = q3-q1
print("Q1=", q1)
print("Q3=", q3)
print("IQR=", iqr)

lowerwhisker=q1-1.5*iqr
upperwhisker = q3+1.5*iqr
print("Upper Whisker", upperwhisker)
print("Lower Whiker", lowerwhisker)
print("Something below", lowerwhisker, ", and something above", upperwhisker, "will not be included in this dataset, and is an outlier.")

newdata=data[data["quant_saved"]<upperwhisker]
allsavings = newdata["quant_saved"].tolist()
meannew = st.mean(allsavings)
mediannew = st.median(allsavings)
modenew = st.mode(allsavings)
sdnew = st.stdev(allsavings)
print("Mean", meannew)
print("Mode", modenew)
print("Median", mediannew)
print("Standard deviation", sdnew)
newgraph = pf.create_distplot([allsavings], ["All savings(without outliers)"], show_hist=False)
newgraph.show()

import random as rand
samplingmeanlist=[]
for i in range(0,1000):
  templist=[]
  for j in range(0,100):
    templist.append(rand.choice(allsavings))
  samplingmeanlist.append(st.mean(templist))
meansample = st.mean(samplingmeanlist)
print(meansample)