import math
def paint_calc(height, width, cover):
     area = height * width
     num_of_cans = math.ceil(area / cover)
     print(f"You'll need {num_of_cans} cans of paint.")

test_height = int(input("Height of wall: "))
test_width = int(input("width of wall: "))
coverage = 5

paint_calc(test_height, test_width, coverage)
# PRIME CHECKER


def prime_checker(number):
    for i in range(2, math.sqrt(number)):
        if number % i == 0:
             print("It's not a prime number.")
         else:
             print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(n)


