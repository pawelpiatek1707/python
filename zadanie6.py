def merge_lists(list1: list, list2: list) -> list:
    merged_list = list(set(list1 + list2))
    new_list = list()
    for num in merged_list:
        new_list.append(num**3)
    return new_list

print(merge_lists([1,2,3,4], [4,5,6,7]))