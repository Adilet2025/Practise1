"""
dates.py
Basic Date and Time operations

date → year, month, day
datetime → date + time
timedelta → difference between dates
strftime → format date to string
strptime → string to datetime
"""

from datetime import date, datetime, timedelta

# Current date and time
now = datetime.now()
print("Now:", now)

# Today's date
today = date.today()
print("Today:", today)

# Difference between dates
d1 = date(2026, 5, 10)
d2 = date(2026, 5, 1)
print("Days difference:", (d1 - d2).days)

# Add 7 days
future = today + timedelta(days=7)
print("After 7 days:", future)

# Format date
print("Formatted:", now.strftime("%Y-%m-%d"))

# Parse string to datetime
parsed = datetime.strptime("2026-05-10", "%Y-%m-%d")
print("Parsed:", parsed)
