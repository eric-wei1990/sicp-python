def sum_natural(n):
    sum, next = 0, 1

    while (next <= n):
        sum = sum + next
        next = next + 1

    return sum

print(sum_natural(1))
print(sum_natural(2))
print(sum_natural(3))
print(sum_natural(4))