# import datetime
# print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__',
#  '__doc__', '__file__', '__loader__', '__name__', '__package__',
#  '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 
#  'timedelta', 'timezone', 'tzinfo']

from datetime import datetime
now = datetime.now()
print(now) # 2024-01-27 23:00:58.785892
day = now.day # 27
month = now.month # 1
year = now.year # 2024
hour = now.hour # 23
minute = now.minute # 3
second = now.second # 42
timestamp = now.timestamp() # 1706376882.324755
print(day, month, year, hour, minute, second)
print('timestamp', timestamp) # timestamp 1706376882.324755
print(f'{day}/{month}/{year}, {hour}:{minute}') # 27/1/2024, 23:4

new_year = datetime(2020,1,1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.hour
second = new_year.second
print(day,month,year,hour,minute,second) # 1 1 2020 0 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}:{second}') # 1/1/2020, 0:0:0


# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
# date_string = 5 December, 2019
# date_object = 2019-12-05 00:00:00
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2024-01-27
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2024
print("Current month:", today.month) # 1
print("Current day:", today.day)     # 27

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
# output
# a = 00:00:00
# b = 10:30:50
# c = 10:30:50
# d = 10:30:50.200555
# Difference B/w Two Points in Time Using
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
    # date_string = 5 December, 2019
    # date_object = 2019-12-05 00:00:00
    # t3 = 86 days, 22:56:50

# Exercises: Day 16
# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
# Get current date and time
now = datetime.now()
# Extract individual components
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = now.timestamp()
print(f'Current Day: {current_day}') # Current Day: 27
print(f"Current Month: {current_month}") # Current Month : 1
print(f"Current Year: {current_year}") # Current Year: 2024
print(f"Current Hour: {current_hour}") # Current Hour: 23
print(f"Current Minute: {current_minute}") # Current Minute: 32
print(f"Current Timestamp: {current_timestamp}") # Current Timestamp: 1706378527.266719
# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
# Format the current date
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}") # Formatted Date: 01/27/2024, 23:32:07
# 3. Today is 5 December, 2019. Change this time string to time.
# Convert a time string to time
time_string = "5 December, 2019"
time_obj = datetime.strptime(time_string, "%d %B, %Y")
print(f"Converted Time: {time_obj}")
# Converted Time: 2019-12-05 00:00:00
# 4. Calculate the time difference between now and new year.
from datetime import timedelta
# Calculate time difference to New Year
new_year = datetime(current_year + 1, 1, 1)
time_difference_to_new_year = new_year - now
print(f"Time Difference to New Year: {time_difference_to_new_year}")
# Time Difference to New Year: 339 days, 0:23:52.080292
# 5. Calculate the time difference between 1 January 1970 and now.
# Calculate time difference to Unix epoch (1 January 1970)
epoch = datetime(1970, 1, 1)
time_difference_to_epoch = now - epoch
print(f"Time Difference to Unix Epoch: {time_difference_to_epoch}")
# # Calculate time difference to Unix epoch (1 January 1970)
epoch = datetime(1970, 1, 1)
time_difference_to_epoch = now - epoch
print(f"Time Difference to Unix Epoch: {time_difference_to_epoch}")
# Time Difference to Unix Epoch: 19749 days, 23:36:42.323677
# 6. Think, what can you use the datetime module for? Examples:
     # Time series analysis
     # To get a timestamp of any activities in an application
     # Adding posts on a blog
# Examples of using the datetime module:
# Time Series Analysis: The datetime module is essential for
# handling time series data, making it easier to manipulate, analyze,
# and visualize temporal data.
# Timestamp for Activities: The module can be used to timestamp events
# or activities in an application, enabling accurate tracking of when 
# specific actions occurred.
# Blog Posts: For blog platforms, the datetime module is handy for
# tracking and displaying the publication date and time of blog posts. 
# It allows sorting and filtering posts based on their chronological 
# order.
# These are just a few examples, and the datetime module is versatile 
# for working with date and time data in various applications.
