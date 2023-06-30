import datetime as dt

#currently data
now = dt.datetime.now()
now = now.year

if now < 2021:
    print('Wear a face mask!')
else:
    print('Optional face mask')

data_of_birth = dt.datetime(year=1999, month=12, day=25, hour = 4)
print(data_of_birth)