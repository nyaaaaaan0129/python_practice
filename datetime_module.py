from datetime import date

today = date.today()
print(today)

day = date(2017, 1, 1)
print(day.weekday())
weekday_str = '月火水木金土日'
print(weekday_str[day.weekday()])