numbers_list: list = [1,2,45,34,12]

def multiply_and_return_for(numbers: list) -> list:
    returned_list: list = []
    for num in numbers:
        returned_list.append(num * 5)

    return returned_list


def multiply_and_return_len(numbers: list) -> list:
    return [number *5 for number in numbers]


print(multiply_and_return_for(numbers_list))

print(multiply_and_return_len(numbers_list))


