import random

number = random.randint(-10000, 10000)
last_number = number % 10
print("Last digit of {} is {}".format(number, last_number))
if last_number > 5:
    print("{} is greater than 5".format(last_number))
elif last_number == 0:
    print("{} is 0".format(last_number))
else:
    print("{} is less than 6 and not 0".format(last_number))
