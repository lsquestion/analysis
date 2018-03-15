import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

names1980=pd.read_csv('./pydata//babynames/yob1880.txt',names=['name','sex','births'])

years=range(1880,2011)

pieces=[]
columns=['name','sex','births']

for year in years:
	path='./pydata//babynames/yob%d.txt'%year
	frame=pd.read_csv(path,names=columns)

	frame['year']=year
	pieces.append(frame)

names=pd.concat(pieces,ignore_index=True)

total_births=names.pivot_table('births',index='year',columns='sex',aggfunc=sum)

def add_prop(group):
	births=group.births.astype(float)

	group['prop']=births/births.sum()
	return group

names=names.groupby(['year','sex']).apply(add_prop)	

np.allclose(names.groupby(['year','sex']).prop.sum(),1)

grouped=names.groupby(['year','sex'])

def get_top1000(group):
	return group.sort_index(by='births',ascending=False)[:1000]

top1000=grouped.apply(get_top1000)

print top1000






