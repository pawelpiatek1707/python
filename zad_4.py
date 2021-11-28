num_list: list = [12, 24, 13, 54, 32, 56, 43, 77, 65, 44]


def return_even_index(numbers: list) -> list:
    returned_elements = list()

    for index in range(0, len(numbers)):
        if index % 2 == 0:
            returned_elements.append(numbers[index])

    return returned_elements


print(return_even_index(num_list))
