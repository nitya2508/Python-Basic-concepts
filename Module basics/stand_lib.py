import random ,math, datetime, calendar, os

courses= ['Math','Physics','Chemistry','Biology']

ramdom_result = random.choice(courses)
print(ramdom_result)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today_date = datetime.date.today()
print(today_date)

leap_year = calendar.isleap(2017)
print(leap_year)

print(os.getcwd())
print(os.__file__) #location of the file