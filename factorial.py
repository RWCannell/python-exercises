# using head recursion
def head_recursion_factorial(n):
    if (n == 1):
        return 1
    temp = head_recursion_factorial(n - 1)
    result = n*temp
    return result

# using tail recursion
def tail_recursion_factorial(n, acc):
    if (n == 0):
        return acc
    return tail_recursion_factorial(n-1, n*acc)

if __name__ == '__main__':
    n = 7
    acc = 1

    print(f"Head Recursion: The factorial of {n} is {head_recursion_factorial(n)}")
    print(f"Tail Recursion: The factorial of {n} is {tail_recursion_factorial(n, acc)}")