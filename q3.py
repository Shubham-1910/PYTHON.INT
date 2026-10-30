#time converter
total_sec = int(input())
houre = total_sec//3600
minute = (total_sec%3600)//60
second = (total_sec%3600)%60
print(houre)
print(minute)
print(second)