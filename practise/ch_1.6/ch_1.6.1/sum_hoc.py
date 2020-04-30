def sum(n, term):
    total, next = 0.0, 1.0
    while next <= n:
        total = total + term(next)
        next = next + 1
    return total

def natural_term(k):
    return k

def sum_natural(n):
    return sum(n, natural_term)

print('------sum_natural')
print(sum_natural(1))
print(sum_natural(2))
print(sum_natural(3))

def cube_term(k):
    return k * k * k

def sum_natural(n):
    return sum(n, cube_term)

print('------sum_cube');
print(sum_natural(1))
print(sum_natural(2))
print(sum_natural(3))

def pi_term(k):
    return 8 / ((4 * k - 3) * (4 * k - 1))

def sum_pi(n):
    return sum(n, pi_term)

print('------sum_pi');
print(sum_pi(1))
print(sum_pi(2))
print(sum_pi(3))
print(sum_pi(100))
print(sum_pi(10000))
print(sum_pi(1000000))