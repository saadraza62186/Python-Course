import time
def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            print(f"Cache hit for arguments: {args}")
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
        pass
    return wrapper

@cache
def long(a, b):
    time.sleep(2)
    return a + b

print(long(1, 2))  # First call, should take time
print(long(1, 2))  # Second call, should be instant