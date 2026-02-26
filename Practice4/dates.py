from datetime import datetime, timedelta   # take datetime and timedelta from datetime module

today = datetime.now()                     # get current date and time
new_date = today - timedelta(days=5)       # subtract 5 days from today

print("Қазіргі күн", today)                # print current date and time
print("5 күн бұрын", new_date)             # print date 5 days ago



from datetime import datetime, timedelta   # import datetime and timedelta

today = datetime.now()                     # get current date and time

yesterday = today - timedelta(days=1)      # subtract 1 day
tomorrow = today + timedelta(days=1)       # add 1 day

print("Yesterday: ", yesterday)            # print yesterday date
print("Tomorrow: ", tomorrow)              # print tomorrow date



from datetime import datetime              # import datetime class

now = datetime.now()                       # get current date and time
print("Now:", now)                         # print full date and time

cleaned = now.replace(microsecond=0)       # remove microseconds (set to 0)
print("Without microsecond:", cleaned)     # print time without microseconds



from datetime import datetime              # import datetime class

date1 = datetime(2026, 2, 20, 12, 0, 0)    # create first date (year, month, day, hour, min, sec)
date2 = datetime(2026, 2, 22, 15, 30, 0)   # create second date

difference = date2 - date1                 # subtract dates (get time difference)

seconds = difference.total_seconds()       # convert difference to seconds
print("Second: ", seconds)                 # print seconds