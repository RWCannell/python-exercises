def binary_search(search_list, item, left, right):
    if (right < left):
        return -1
    middle = (left + right)//2
    if (search_list[middle] == item):
        return middle
    if (search_list[middle] < item):
        return binary_search(search_list, item, middle + 1, right)
    else:
        return binary_search(search_list, item, left, middle - 1)

if __name__ == '__main__':
    search_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 67, 71, 73, 79, 83, 89]
    item = 71
    left = 14
    right = 22

    print(f"Number {item} is at index {binary_search(search_list, item, left, right)} of the search list.")
