import datetime
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# we know that 2520 is the smallest divisible by 1-10 so we can start with that as seed and increment by that amount
def smallest_number(numbers):
        for num in range(2520,999999999,2520):
            if all(num % x == 0 for x in numbers): 
                return num

start = datetime.datetime.now()
print(smallest_number([11, 13, 14, 16, 17, 18, 19, 20]))
stop = datetime.datetime.now()
print(stop - start)