import random

def partition(numbers, left_index, right_index):
    # select a random index from the interval which will be the pivot
    random_index = random.randint(left_index, right_index)

    # swap the pivot value with the last number in the list
    numbers[random_index], numbers[right_index] = numbers[right_index], numbers[random_index]

    # store the index
    stored_index = left_index
    for i in range(left_index, right_index + 1):
        if numbers[i] < numbers[right_index]:
            # swap the value at the current index (i) with the value at the stored index
            numbers[i], numbers[stored_index] = numbers[stored_index], numbers[i]

            # increment the stored index
            stored_index += 1
    
    # move pivot to the last index of the partitioned list
    numbers[stored_index], numbers[right_index] = numbers[right_index], numbers[stored_index]

    return stored_index

# We'd like to find the k-th smallest number in a list of numbers
def quick_select(numbers, left_index, right_index, k):
    if left_index == right_index:
        return numbers[left_index]
    
    pivot_index = partition(numbers, left_index, right_index)

    if k == pivot_index:
        return numbers[k]
    elif k < pivot_index:
        return quick_select(numbers, left_index, pivot_index - 1, k)
    else:
        return quick_select(numbers, pivot_index + 1, right_index, k) 

if __name__ == '__main__':
    numbers = [7, 4, -1, 2, 9, -3, 3, -2, 6, -5, 10, 0]
    left_index = 0
    right_index = len(numbers) - 1
    k = 12

    print(f"Select the {k}-th smallest number in {numbers}: {quick_select(numbers, left_index, right_index, k - 1)}")
