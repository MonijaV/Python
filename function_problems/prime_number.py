def prime_number(num):
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        return "Prime Number"
    else:
        return "Not a Prime Number"
num = int(input("Enter a number: "))
print(prime_number(num))