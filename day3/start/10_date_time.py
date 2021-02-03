# https://www.programiz.com/python-programming/datetime
# https://www.programiz.com/python-programming/datetime/strptime

# # 01
# from datetime import datetime
# now = datetime.now()
# print(now)



# # 02
# from datetime import datetime
# today = datetime.today().date()
# print(today)
# now_time = datetime.now().time()
# print(now_time)



# # 03
# from datetime import datetime
# now = datetime.now()
# then = datetime(2021, 5, 23)
# delta = then-now
# print(delta.days)
# print(delta.seconds)



# 04
# from datetime import datetime, timedelta
# add_days=120
# now = datetime.now()
# delta = timedelta(days=add_days)
# new_date = now + delta
# print(new_date)


# # 05
# # datetime to string 
# from datetime import datetime
# datetime_for_string = datetime(2021,10,1,0,0)
# datetime_string_format = '%b %a %d %Y, %H:%M:%S'
# data = datetime.strftime(datetime_for_string,datetime_string_format)
# print(data, type(data))


# # 06
# # string to datetime 
# from datetime import datetime
# datetime_string = 'Oct 1 2021, 00:00:00'
# datetime_string_format = '%b %d %Y, %H:%M:%S'
# data = datetime.strptime(datetime_string, datetime_string_format)
# print(data, type(data))

# How can I convert this pattern 20210131 (YYYYMMDD) to a particular date?
# from datetime import datetime
# s = "20210131"
# p = "%Y%m%d"

# data = datetime.strptime(s, p).date();
# print(data)

# p = "%b"
# data = datetime.strftime(data, p)
# print(data)
