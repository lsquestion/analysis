import pandas as pd 

names1980=pd.read_csv('./pydata/ch02/usagov_bitly_data2012-03-16-1331923249.txt',names=['name','sex','births'])


print names1980.groupby('sex').births.sum()