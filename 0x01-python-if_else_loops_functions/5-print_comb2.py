#!/usr/bin/python3
for number in range(0, 100):
     if number == 99:
        print("{}".format(number))
     else:
        print(f'{number:02d}', end=", ")
        