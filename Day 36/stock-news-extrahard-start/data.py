import datetime

date_now = datetime.datetime.now().date()
date_yesterday = date_now - datetime.timedelta(days=1)
print(date_now)
print(date_yesterday)