def pythagorean_triple(n):
    for i in range(1, int(n / 3) + 1):      
        for j in range(i + 1,  int(n / 2) + 1):  
            k = n - i - j 
            if (i * i + j * j == k * k):  
                return (i, j, k)

n = 1000
result = pythagorean_triple(n) 
print(result[0] * result[1] * result[2])

