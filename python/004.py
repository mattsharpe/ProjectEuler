from datetime import datetime

def largest_palindromic_number():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, i, -1):
            result = i*j
            if result < largest:
                continue
            if isPalindrome(result):
                largest = result
    return largest

def isPalindrome(number):
    return str(number) == ''.join(reversed(str(number)))

startTime = datetime.now()

print(largest_palindromic_number())    
print(datetime.now() - startTime)