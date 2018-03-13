import pandas as pd 

unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('./pydata/ch02/movielens/users.dat',sep='::',header=None,names=unames)
rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('./pydata/ch02/movielens/ratings.dat',sep='::',header=None,names=rnames)
mnames=['movie_id','title','genres']
movies=pd.read_table('./pydata/ch02/movielens/movies.dat',sep='::',header=None,names=mnames)

print users[:5]
print ratings[:5]
print movies[:5]