# Python National Stock Exchange (NSE) Data Extraction
This is a mini project which utilizes python to extract files from an open website in an automated manner.

The Files can be downloaded from the nsebhavcopy site as mentioned in code using the nse_bhavcopy_pr_daily.py . It is a code written in loop to download each file as per the year/month/day specified. We need to only specify the start year and it will start downloading all files from there till current year. There is 1 file created per day in the website link, with the respective open/close amount details for the various public companies actively listed on that day.

Once all files have been downloaded and stored in the location, we can run the second script csv_merge.py to merge all the respective files into 1 file per year, as it easier to manage and query.

![image](https://github.com/RandomlyCreative/Python_nse_data_extraction/assets/39943529/746a24c2-fcd8-45c8-9b43-3b63ff6e5539)

