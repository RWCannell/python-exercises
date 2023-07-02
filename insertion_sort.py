def insertion_sort(unsorted):
    unsorted_length = len(unsorted)
    
    i = 1
    while i < unsorted_length:
        j = i
        while j > 0 and unsorted[j - 1] > unsorted[j]:
            temp = unsorted[j]
            unsorted[j] = unsorted[j - 1]
            unsorted[j - 1] = temp
            j -= 1
        i += 1

    return unsorted

if __name__ == "__main__":
    unsorted_list = [3, 6, 4, 1, 7, 0, 5, 8, 2, 9]
    sorted_list = insertion_sort(unsorted_list)
    print(sorted_list)