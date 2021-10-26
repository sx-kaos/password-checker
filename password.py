import datetime
from datetime import datetime


password = input('Enter length of password: ')
now = datetime.now()
length = 92 ** int(password)
x = 1
print(f'{length} possible passwords of that length')
print("this make take some time depending on the length of your password")
while True:
    x += 1
    if x == length:
        end = datetime.now()
        print(f'if the hackers started at {now} they would finish at {end}')
        input()
        break
    elif x != length:
        pass