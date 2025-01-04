import time
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is being called with arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

def timer(func):
       def wrapper(*args, **kwargs):
           start_time = time.time()
           result = func(*args, **kwargs)
           end_time = time.time()
           print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
           return result
       return wrapper

def validate_inputs(func):
       def wrapper(*args, **kwargs):
           if any(arg < 0 for arg in args):
               raise ValueError("All arguments must be non-negative")
           return func(*args, **kwargs)
       return wrapper


# Applying the decorator to a function
@log_decorator
@timer
@validate_inputs
def add(a, b):
    return a + b

# Using the decorated function

result = add(5, 3)
print(f"Result: {result}")
