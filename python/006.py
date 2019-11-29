# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import datetime

def sum_of_squares(numbers):
    return sum(pow(x,2) for x in numbers)

def square_of_sums(numbers):
    return pow(sum(numbers), 2)

numbers = range(1,101)

start = datetime.datetime.now()
print(square_of_sums(numbers) - sum_of_squares(numbers))
stop = datetime.datetime.now()

print(stop - start)