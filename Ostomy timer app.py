from time import sleep
import random

# input

input_time = float(input("When was your last meal in seconds:\t"))
meal_size = input("Portion size (1)big meal, (2)medium meal, (3)snack):\t")


# process

if meal_size == "1":
    output_time = random.randint(40,60)
elif meal_size == "2":
    output_time = random.randint(20,40)
elif meal_size == "3":
    output_time = random.randint(10,20)

resultant_time = output_time - input_time

print(int(resultant_time), "seconds left")

# output

i = resultant_time

while i > 0: 
    sleep(1)
    i -= 1
    print(int(i), "seconds left")

print("It's time to change your ostomy bag!")
