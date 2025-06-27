#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
 if number[-1:] > 5:
    print("Last digit of {} is {} and is greater than 5".format(str(num),number[-1:]))
elif number[-1:] == 0:
    print("Last digit of {} is {} and is 0".format(str(num),number[-1:]))
elif number[-1:] <6 and number[-1:] !=0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(str(number),number[-1:]))
