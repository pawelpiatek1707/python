def check_existance(numbers_list: list, number: int)->bool:
    returned_value: bool = False
    for num in numbers_list:
        if num == number:
            returned_value = True
            break
    return returned_value

print(check_existance([1,2,3,4,5], 8))
