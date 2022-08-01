import datetime
n=input()
datetime_obj= datetime.datetime.strptime(n,"%d/%m/%Y")
year=datetime_obj.year
last_day_obj=datetime.datetime(year,12,31)
days_left=last_day_obj - datetime_obj
print(days_left)
