num = 30
fibonacci = [1,1]

for i in range(2, 30):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci)