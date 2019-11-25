def multiples_of_3_or_5():
    return sum(i for i in range(0,1000) if i%3 ==0 or i%5 == 0)

print(multiples_of_3_or_5())