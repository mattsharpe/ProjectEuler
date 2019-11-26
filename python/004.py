def largest_palindromic_number():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, i, -1):
            result = i*j
            if result < largest or (i % 11 !=0 and j % 11 !=0):
                continue
            if isPalindrome(result):
                largest = result
    return largest

def isPalindrome(number):
    return str(number) == ''.join(reversed(str(number)))

print(largest_palindromic_number())    