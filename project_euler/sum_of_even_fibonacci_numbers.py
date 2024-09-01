# function for calculating the nth Fibonacci number
def calculate_nth_fibonacci_number(n):
    if (n == 0) or (n == 1):
        return 1
    return calculate_nth_fibonacci_number(n-2) + calculate_nth_fibonacci_number(n-1)

# return a list of Fibonacci numbers
def list_fibonacci_numbers(n):
    fibonacci_numbers = []
    for i in range(n+1):
        fibonacci_number = calculate_nth_fibonacci_number(i)
        fibonacci_numbers.append(fibonacci_number)
    return fibonacci_numbers

# return a list of even Fibonacci numbers
def list_even_fibonacci_numbers(n):
    even_fibonacci_numbers = []
    for i in range(n+1):
        fibonacci_number = calculate_nth_fibonacci_number(i)
        if fibonacci_number % 2 == 0:
            even_fibonacci_numbers.append(fibonacci_number)
    return even_fibonacci_numbers

# return sum of Fibonacci numbers
def calculate_sum_of_fibonacci_numbers(n):
    fibonacci_numbers = list_fibonacci_numbers(n)
    sum = 0
    for i in fibonacci_numbers:
        sum += i
    return sum

# return a list of Fibonacci numbers less than upper bound
def list_fibonacci_numbers_less_than_upper_bound(upper_bound):
    fibonacci_numbers = []
    fibonacci_number_upper_bound_exceeded = False
    iteration_number = 1
    while not fibonacci_number_upper_bound_exceeded:
        iteration_number += 1
        fibonacci_number = calculate_nth_fibonacci_number(iteration_number)
        if fibonacci_number >= upper_bound:
            fibonacci_number_upper_bound_exceeded = True
            break
        fibonacci_numbers.append(fibonacci_number)
    return fibonacci_numbers

# sum even-valued Fibonacci numbers less than upper bound
def calculate_sum_of_even_fibonacci_numbers_less_than_upper_bound(upper_bound):
    even_fibonacci_numbers = []
    fibonacci_number_upper_bound_exceeded = False
    iteration_number = 0
    while not fibonacci_number_upper_bound_exceeded: 
        iteration_number += 1
        fibonacci_number = calculate_nth_fibonacci_number(iteration_number)
        if fibonacci_number >= upper_bound:
            fibonacci_number_upper_bound_exceeded = True
            break
        if fibonacci_number % 2 == 0:
            even_fibonacci_numbers.append(fibonacci_number)
    print(f"List of even Fibonacci numbers less than upper bound {upper_bound} after {iteration_number} iterations: {even_fibonacci_numbers}")

    sum_of_even_fibonacci_numbers = 0
    for i in even_fibonacci_numbers:
        sum_of_even_fibonacci_numbers += i
    return sum_of_even_fibonacci_numbers

if __name__ == '__main__':
    n = 10
    upper_bound = 1000000
    nth_fibonacci_number = calculate_nth_fibonacci_number(n)
    fibonacci_numbers = list_fibonacci_numbers(n)
    even_fibonacci_numbers = list_even_fibonacci_numbers(n)
    sum_of_fibonacci_numbers = calculate_sum_of_fibonacci_numbers(n)
    fibonacci_numbers_less_than_upper_bound = list_fibonacci_numbers_less_than_upper_bound(upper_bound)
    sum_of_even_fibonacci_numbers_less_than_upper_bound = calculate_sum_of_even_fibonacci_numbers_less_than_upper_bound(upper_bound)
    print(f"The nth Fibonacci number for n = {n} is: {nth_fibonacci_number}")
    print(f"Sequence of Fibonacci numbers for n = {n} is: {fibonacci_numbers}")
    print(f"Sequence of even Fibonacci numbers for n = {n} is: {even_fibonacci_numbers}")
    print(f"Sum of Fibonacci numbers for n = {n} is: {sum_of_fibonacci_numbers}")
    print(f"Sequence of Fibonacci numbers less than the upper bound {upper_bound} is: {fibonacci_numbers_less_than_upper_bound}")
    print(f"Sum of even Fibonacci numbers less than the upper bound {upper_bound} is: {sum_of_even_fibonacci_numbers_less_than_upper_bound}")