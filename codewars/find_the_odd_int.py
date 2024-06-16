# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.
# Examples

# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    # initialise empty dictionary
    number_of_occurrences = {}
    
    # initialise dictionary of all values being 0
    for i in seq:
        number_of_occurrences[i] = 0
    for i in seq:
        if i in number_of_occurrences.keys():
            number_of_occurrences[i] = number_of_occurrences[i] + 1

    for key in number_of_occurrences.keys():
        if (number_of_occurrences[key] % 2) != 0:
            return key

if __name__ == '__main__':
    sequence = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
    solution = find_it(sequence)
    print(f"The solution is {solution}.")