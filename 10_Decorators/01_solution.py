import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds)")
        return result
    return wrapper

@timer
def example_func(n):
    time.sleep(n)  # Simulate a time-consuming operation

example_func(2)  # Call the function to see the timer in action
