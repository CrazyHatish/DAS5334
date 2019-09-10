with open('words.txt', 'r') as file:
    for line in file:
        if len(line.strip()) > 20:
            print(line.strip())
