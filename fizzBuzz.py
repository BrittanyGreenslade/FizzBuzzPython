def fizz_buzz(num):
    # % means divisible by
    if (num % 5 == 0 and num % 3 == 0):
        print("FizzBuzz")
    elif (num % 5) == 0:
        print("Buzz")
    elif (num % 3) == 0:
        print("Fizz")
    else:
        print("Not divisible")


numbers = [12, 7, 8, 25, 9, 15, 22, 18, 10, 14, 30, 11, 26, 32, 50, 19, 21]

for number in numbers:
    fizz_buzz(number)
