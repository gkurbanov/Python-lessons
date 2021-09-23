f = open('data-task2.txt', 'r')

i = 0
for line in f:
    word_length = len(line)
    print(f"Строчка номер {i}, слово {line}, символов {word_length}\n", end='')
    i += 1

f.close()
