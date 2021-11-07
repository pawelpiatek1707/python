num_list: list = [12,24,13,54,32,56,43,77,65,44]

def return_even(numbers: list) -> list:
    even_numbers = list()

    for num in range(0, len(numbers)):
        if numbers[num] % 2 == 0:
            even_numbers.append(numbers[num])

    return even_numbers


print(return_even(num_list))