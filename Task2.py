
import time

# Ввод секунд
user_entered_seconds = int(input('Введите секунды - '))

print(time.strftime("%H:%M:%S", time.gmtime(user_entered_seconds)))