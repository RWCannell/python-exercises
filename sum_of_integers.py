# sum of first n integers using iteration
def iterative_sum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

# sum of first n integers using recursion
def recursive_sum(n):
    if (n == 1):
        return 1
    return n + recursive_sum(n-1) 

if __name__ == '__main__':
    n = 100

    print(f"Iterative Sum of first {n} integers: {iterative_sum(n)}")
    print(f"Recursive Sum of first {n} integers: {recursive_sum(n)}")