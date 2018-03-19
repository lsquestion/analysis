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
'''
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False)
参数说明 
objs: series，dataframe或者是panel构成的序列lsit 
axis： 需要合并链接的轴，0是行，1是列 
join：连接的方式 inner，或者outer
ignore_index:是否重建索引
'''
total_births=names.pivot_table('births',index='year',columns='sex',aggfunc=sum)

def add_prop(group):
	births=group.births.astype(float)

	group['prop']=births/births.sum()
	return group

names=names.groupby(['year','sex']).apply(add_prop)	

np.allclose(names.groupby(['year','sex']).prop.sum(),1)

grouped=names.groupby(['year','sex'])
	
def get_top1000(group):
	return group.sort_values(by='births',ascending=False)[:1000]

top1000=grouped.apply(get_top1000)

boys=top1000[top1000.sex=='M']
girls=top1000[top1000.sex=='F']

total_births=top1000.pivot_table('births',index='year',columns='name',aggfunc=sum)
subset=total_births[['John','Harry','Mary','Marilyn']]
#subset.plot(subplots=True,figsize=(12,10),grid=False,title="Number of births per year")

#plt.show()
table=top1000.pivot_table('prop',index='year',columns='sex',aggfunc=sum)
#table.plot(title='Sum of table1000.prop by year and sex',yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))
#plt.show()
#df=boys[boys.year==2010]

#prop_cumsum=df.sort_values(by='prop',ascending=False).prop.cumsum()
#print(prop_cumsum.searchsorted(0.5))
#df=boys[boys.year==1900]
#in1900=df.sort_values(by='prop',ascending=False).prop.cumsum()
def get_quantitle_count(group,q=0.5):
	group=group.sort_values(by="prop",ascending=False)
	return group.prop.cumsum().searchsorted(q)[0]+1

diversity=top1000.groupby(['year','sex']).apply(get_quantitle_count)
diversity=diversity.unstack('sex')
#print(diversity)

#diversity.plot(title="Number of popular names in top 50%")
#plt.show()
get_last_letter=lambda x:x[-1]

last_letters=names.name.map(get_last_letter)

last_letters.name='last_letters'

table=names.pivot_table('births',index=last_letters,columns=['sex','year'],aggfunc=sum)

subtable=table.reindex(columns=[1910,1960,2010],level='year')
#print(subtable.sum())
letter_prop=subtable/subtable.sum().astype(float)
import matplotlib.pyplot as plt

#fig,axes=plt.subplots(2,1,figsize=(10,8))
#letter_prop['M'].plot(kind='bar',rot=0,ax=axes[0],title='Male')
#letter_prop['F'].plot(kind='bar',rot=0,ax=axes[1],title='Female',legend=False)
letter_prop=table/table.sum().astype(float)
dny_ts=letter_prop.ix[['d','n','y'],'M'].T
#print(dny_ts.head())
#dny_ts.plot()
#plt.show()
all_names=top1000.name.unique()
mask=np.array(['lesl' in x.lower() for x in all_names])

lesley_like=all_names[mask]

filtered=top1000[top1000.name.isin(lesley_like)]

filtered.groupby('name').births.sum()
table=filtered.pivot_table('births',index='year',columns='sex',aggfunc='sum')
table=table.div(table.sum(1),axis=0)

table.plot(style={'M':'k-','F':'k--'})

plt.show()


