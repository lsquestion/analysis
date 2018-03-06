import json

path='./pydata/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

f=open(path).readline()

#print f 

records=[json.loads(line) for line in open(path)]

#time_zones=[rec['tz'] for rec in records if 'tz' in rec]

from pandas import DataFrame,Series

import pandas as pd;import numpy as np 

frame=DataFrame(records)

print frame['tz'][:10]