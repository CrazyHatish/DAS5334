from time import time

word_list = []

start_time = time()

with open('words.txt', 'r') as file:
	for line in file:
		word_list.append(line.strip())

end_time = time()

print("Elapsed time for append(): {}".format(end_time - start_time))

word_list = []

start_time = time()

with open('words.txt', 'r') as file:
	for line in file:
		word_list = word_list + [line.strip()]

end_time = time()

print("Elapsed time for +: {}".format(end_time - start_time))