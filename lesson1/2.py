time = int(input('Время в секундах: '))
hours = time // 3600
minutes = (time - (hours * 3600)) // 60
seconds = time - (hours * 3600) - (minutes * 60)
if hours < 10:
    hours = str(0) + str(hours)
if minutes < 10:
    minutes = str(0) + str(minutes)
if seconds < 10:
    seconds = str(0) + str(seconds)
print(f"{hours}:{minutes}:{seconds}")
