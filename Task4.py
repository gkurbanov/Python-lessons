# Пользователь вводит строку
# Текст рыба - It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages
word_string = input('Введите строку из слов - ')
words = word_string.split()
print(words)


i = 1
for key in words:
    print(i, '>', key[:10])
    i += 1
