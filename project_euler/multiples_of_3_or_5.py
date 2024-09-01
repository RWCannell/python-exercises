# Function for finding the sum of multiples of 3 or 5 between 1 and n (excluding n)
def calculate_sum_of_multiples_of_3_or_5(n):
    sum = 0
    multiples = []
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            multiples.append(i)
    print(f"Multiples of 3 or 5 less than {n}: {multiples}")

    for j in multiples:
        sum += j
    return sum

if __name__ == '__main__':
    n = 1000
    sum_of_multiples_of_3_or_5 = calculate_sum_of_multiples_of_3_or_5(n)
    print(f"Sum of multiples of 3 or 5 less than {n}: {sum_of_multiples_of_3_or_5}")