a = lambda b: b + 4
print(a(4))


c = lambda d, e: d + e
print(c(7, 8))


def ghost_numbers(n):
    return lambda f: f * n


double_num = ghost_numbers(2)
print(double_num(20))
