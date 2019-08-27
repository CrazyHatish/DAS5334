import time

current_time = time.time()

days = current_time // 60 // 60 // 24
hours = (current_time - days * 60 * 60 * 24) // 60 // 60
minutes = (current_time - days * 60 * 60 * 24 - hours * 60 * 60) // 60
seconds = (current_time - days * 60 * 60 * 24 - hours * 60 * 60 - minutes * 60)

print("{} days, {} hours, {} minutes, {} seconds since epoch".format(days, hours, minutes, seconds))
