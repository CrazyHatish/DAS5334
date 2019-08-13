from math import pi

#2.1

radius = 5
volume = 4/3 * pi * (radius ** 3)
print(volume)

#2.2

cover_price = 24.95
bookstore_price = cover_price * 0.6
num_copies = 60
shipping = 3 + (num_copies - 1) * 0.75

total_cost = bookstore_price * num_copies + shipping
print("${:.2f}".format(total_cost))

#2.3

leave_time = 6*60**2 + 52*60
easy_pace = 8*60 + 15
tempo = 7*60 + 12

arrival_in_seconds = leave_time + easy_pace + tempo*3 + easy_pace
arrival_hour = arrival_in_seconds // 60 // 60
arrival_minute = (arrival_in_seconds - arrival_hour*60**2) // 60
arrival_second = (arrival_in_seconds - arrival_hour*60**2 - arrival_minute*60)
arrival_time = "{:02}:{:02}:{:02}".format(arrival_hour, arrival_minute, arrival_second)
print(arrival_time)
