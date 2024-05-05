def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def goldbach(n):
    primes = [x for x in range(2, n) if is_prime(x)]
    pairs = []
    for a in primes:
        if (n - a) in primes:
            pairs.append((a, n - a))
        if len(pairs) > 100:
            pairs.append("......")
            break
    return pairs


def main():
    try:
        n = int(input("Enter a positive even number: "))
        if n % 2 != 0:
            print("The number should be even")
            return
        pairs = goldbach(n)
        if not pairs:
            print(f"Goldbach's conjecture may not be valid for {n}.")
            return
        print(f"Goldbach's conjecture is valid for {n}. The following pairs of primes sum to {n}:")
        for pair in pairs:
            print(pair)
        return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return


if __name__ == "__main__":
    main()
