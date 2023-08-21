def fibonacci_series(limit):
    fib_series = [0, 1]
    while True:
        next_fib_no = fib_series[-1] + fib_series[-2]
        if next_fib_no <= limit:
            fib_series.append(next_fib_no)
        else:
            break
    return fib_series[1:]  # Exclude the first element (0)

limit = 50
fib_series = fibonacci_series(limit)
print(' '.join(map(str, fib_series)))
