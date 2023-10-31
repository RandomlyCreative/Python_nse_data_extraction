import os
import requests
import csv
import pandas as pd
import io
from calendar import monthrange, month_abbr
import zipfile
import datetime

current_time=datetime.datetime.now()
current_day=current_time.day
current_month=current_time.month
current_year=current_time.year

year_lst = []
for i in range(1994,current_year+1):
    year_lst.append(i)

month_lst = [1,2,3,4,5,6,7,8,9,10,11,12]
headers = {
    'user-agent':"Mozilla/5.0 ...",
    'accept': '"text/html,application...',
    'referer': 'https://...',
}

for i in range(0,len(year_lst)):
    if year_lst[i]>current_year:
        break
    p_yr='year: '+str(year_lst[i])
    path='D:\\nse_bhavcopy\\pr\\'+str(year_lst[i])+'\\'
    if not os.path.exists(path):
        os.makedirs(path)
    print(p_yr)
    for f in range(0,len(month_lst)):
        if month_lst[f]>current_month and year_lst[i]==current_year:
            break
        p_m='month: '+str(month_abbr[month_lst[f]])
        print(p_m)
        for g in range(1,monthrange(year_lst[i], month_lst[f])[1] + 1):
            if month_lst[f]>=current_month and g>current_day and year_lst[i]==current_year:
                break
            month = (month_abbr[month_lst[f]]).upper()
            year = str(year_lst[i])
            if g<10:
                day= '0'+str(g)
            else:
                day= str(g)
            filename = 'PR'+day+month+year+'bhav.csv'
            res = requests.get('https://www1.nseindia.com/archives/equities/bhavcopy/pr/'+filename+'.zip', headers=headers)
            try:
                df = pd.DataFrame()
                df = pd.read_csv(io.BytesIO(res.content), compression="zip")
                df.to_csv(path+month+'_'+filename)
                print(p_yr+' '+p_m+' '+day+': SUCCESS')
            except:
                    print(p_yr+' '+p_m+' '+day+ ': ERROR')
                    print(res.content)
                    
---------------------------------------------------------------------------------------------------------------------------------------------------------

<a href="/archives/equities/bhavcopy/pr/PR170822.zip" target="new">PR170822.zip</a>

https://www1.nseindia.com/archives/equities/bhavcopy/pr/PR170822.zip

year = '22'
month = '08'
day = '08'
filename = 'PR'+day+month+year
path='D:\\nse_bhavcopy\\pr\\'

headers = {
    'user-agent':"Mozilla/5.0 ...",
    'accept': '"text/html,application...',
    'referer': 'https://...',
}

res = requests.get('https://www1.nseindia.com/archives/equities/bhavcopy/pr/'+filename+'.zip', headers=headers)

from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'https://www1.nseindia.com/archives/equities/bhavcopy/pr/'+filename+'.zip'
with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall(path)

zip_file = zipfile.ZipFile(io.BytesIO(res.content), compression="zip")
dfs = {text_file.filename: pd.read_csv(zip_file.open(text_file.filename))
       for text_file in zip_file.infolist()
       if text_file.filename.endswith('.csv')}


df = pd.read_csv(io.BytesIO(res.content), compression="zip")
df.to_csv(path+filename)
print(res.content)