def find_primitive_root(p):
    primitive_roots = []
    factors = find_prime_factors(p - 1)

    for r in range(2, p):
        is_primitive_root = all(pow(r, (p - 1) // factor, p) != 1 for factor in factors)

        if is_primitive_root:
            primitive_roots.append(r)

    return primitive_roots


def find_prime_factors(n):
    factors = []
    i = 2

    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    return factors


def mod_pow(base, exponent, modulus):
    result = 1
    base %= modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus

        exponent //= 2
        base = (base * base) % modulus

    return result


def main():
    prime_number = 13  # Replace this with your desired prime number
    primitive_roots = find_primitive_root(prime_number)

    if primitive_roots:
        print(f"Primitive Roots modulo {prime_number} are: {primitive_roots}")
    else:
        print(f"No primitive roots found for {prime_number}")


if _name_ == "_main_":
    main()