import time

# A Decorator is a function that takes in a function and retuns a function, typically modifying somewhat the behavior of the original.

# For example lets take this function that squares numbers
def square_a_lot_of_numbers(n):
    squared = [i ** 2 for i in range(n)]
    return squared


# To time it, we could write a timing decorator like so:
def time_function_decorator(original_function):
    def the_decorated_function(*args, **kwargs):
        start_time = time.perf_counter()
        value = original_function(*args, **kwargs)
        stop_time = time.perf_counter()
        print(f"The runtime was {stop_time - start_time}")
        return value

    return the_decorated_function


decorated_square = time_function_decorator(square_a_lot_of_numbers)


decorated_square(10000000)