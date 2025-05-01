def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling function '{func.__name__}' with arguments: {args_value}, {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper
@debug
def greet(name, greet):
    print(f"{greet}, {name}!")
    
greet("saad", "Hello")