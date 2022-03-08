n = 0
while (n + 1) * (n + 1) < 1234:
    n += 1
print("n = ", n, "n² = ", n * n)
print("n+1 = ", n + 1, "n² = ", (n + 1) * (n + 1))

n_square = [i * i for i in range(n + 1)]
print(n_square)

divisible_sum = [k for k in range(n + 1)
                 if (k + n_square[k]) % 4 == 0]
print(divisible_sum)