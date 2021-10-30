import time
import os 
from os import system
import datetime
from datetime import datetime

def main():
    os.system('title password checker')
    os.system('cls')
    try:
        password = int(input('Enter length of password: '))
        now = datetime.now()
        length = 92 ** int(password)
        x = 1
        print(f'{length} possible passwords of that length')
        while True:
            x += 1
            if x == length:
                end = datetime.now()
                print(f'if the hackers started at {now} they would finish at {end}')
                input()
                main()
            elif x != length:
                pass
    except ValueError:
        print(f'please enter a number')
        time.sleep(2)
        main()

main()
