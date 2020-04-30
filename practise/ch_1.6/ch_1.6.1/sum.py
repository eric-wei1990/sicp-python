def sum_natural(n):
    sum, next = 0, 1

    while (next <= n):
        sum = sum + next
        next = next + 1

    return sum
print('----sum_natual-----')
print(sum_natural(1))
print(sum_natural(2))
print(sum_natural(3))
print(sum_natural(4))

def sum_cube(n):
    sum, next = 0, 1

    while (next <= n):
        sum = sum + next * next * next
        next = next + 1

    return sum

print('----sum_cube-----')
print(sum_cube(1))
print(sum_cube(2))
print(sum_cube(3))
print(sum_cube(4))

def sum_pi(n):
    sum, next = 0, 1.0

    while (next <= n):
        sum = sum + 8 / ((4 * next - 3) * (4 * next - 1))
        next = next + 1

    return sum

def pi_sum(n):
    total, k = 0, 1.0
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1

    return total

print('----pi_sum-----')
print(pi_sum(100))