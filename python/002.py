calculated = [0,1]

def fibonacci(n):
    if n<=len(calculated):
        return calculated[n-1]
    else:
        next = fibonacci(n-1)+fibonacci(n-2)
        calculated.append(next)
        return next


limit = 4000000
current = 0
count = 1
answers = []

while current < limit:
    current = fibonacci(count)
    if current %2 == 0:
        answers.append(current)
    count+=1

print(sum(answers))
