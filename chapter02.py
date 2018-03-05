import json

path='./pydata/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

f=open(path).readline()

#print f 

records=[json.loads(line) for line in open(path)]

print records[0]