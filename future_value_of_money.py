from math import exp

# x is the initial amount of money
# n is the number of years (discrete)
# t is the amount of time (continuous)
# r is the interest rate

def discrete_future_value(x, r , n):
    return x*(1 + r)**n

def discrete_present_value(x, r , n):
    return x*(1 + r)**-n

def continuous_future_value(x, r , t):
    return x*exp(r*t)

def continuous_present_value(x, r , t):
    return x*exp(-r*t)

if __name__ == '__main__':
    x = 50000
    n = 3
    t = 3 
    r = 0.09

    print(f"Discrete Model: Future Value of R{x}: R{discrete_future_value(x, r , n)}")
    print(f"Discrete Model: Present Value of R{x}: R{discrete_present_value(x, r , n)}")
    print(f"Continuous Model: Future Value of R{x}: R{continuous_future_value(x, r , n)}")
    print(f"Continuous Model: Present Value of R{x}: R{continuous_present_value(x, r , n)}")