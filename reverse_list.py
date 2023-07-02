# function that reverses the elements in a list in-place
def reverse_list(items):
    items_length = len(items)
    low_index = 0
    high_index = items_length - 1

    while low_index < high_index:
        swap_items(items, low_index, high_index)
        low_index += 1
        high_index -= 1

    return items

# function for swapping two items in a list
def swap_items(items, first_index, second_index):
    temp = items[second_index]
    items[second_index] = items[first_index]
    items[first_index] = temp

if __name__ == "__main__":
    list_of_items = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]
    reversed_list = reverse_list(list_of_items)
    print(reversed_list)