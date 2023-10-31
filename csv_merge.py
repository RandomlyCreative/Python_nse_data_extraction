import glob
import os
import csv
import pandas as pd
import io
import datetime

current_time=datetime.datetime.now()
current_day=current_time.day
current_month=current_time.month
current_year=current_time.year

path_yr = 'D:\\nse_bhavcopy\\cm_yearly\\'
year_lst = []

if not os.path.exists(path_yr):
    os.makedirs(path_yr)

for j in range(1994,current_year+1):
    year_lst.append(j)

for i in range(0,len(year_lst)):
    if year_lst[i]>current_year:
        break
    p_yr='year: '+str(year_lst[i])
    path='D:\\nse_bhavcopy\\cm\\'+str(year_lst[i])+'\\'
    df = []
    files = glob.glob(path+"*.csv")
    for f in files:
        csv = pd.read_csv(f)
        df.append(csv)
    df = pd.concat(df)
    df.to_csv(path_yr+str(year_lst[i])+'_nse_bhavcopy.csv')
    print(p_yr)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

import glob
import os
import csv
import pandas as pd
import io
import datetime

current_time=datetime.datetime.now()
current_day=current_time.day
current_month=current_time.month
current_year=current_time.year

path='D:\\nse_bhavcopy\\cm_yearly\\'
dff = pd.DataFrame()
df = []
files = glob.glob(path+"*.csv")
for f in files:
    csv = pd.read_csv(f)
    df.append(csv)
df = pd.concat(df)
df.to_csv('D:\\nse_bhavcopy\\'+'1994nov_2022aug_cmbhavcopy_1.csv')

df = pd.concat(pd.read_csv(fl) for fl in files)
df.to_csv('D:\\nse_bhavcopy\\'+'1994nov_2022aug_cmbhavcopy.csv', index = False)

print('done')