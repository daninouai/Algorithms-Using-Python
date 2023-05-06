import timeit

start = timeit.default_timer()

m = int(input('Enter n:'))


# function for fibonacci Divide and Conquer
def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(f'Res is {fib(m)}')

stop = timeit.default_timer()

print('Time: ', stop - start)
