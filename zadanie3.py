def check_even(num: int)-> bool:
    return num % 2 == 0

is_even = check_even(4)

if is_even:
    print('liczba jest parzysta')
else:
    print('liczba jest nieparzysta')