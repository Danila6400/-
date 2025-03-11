def double(func):
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double
def return_number(num):

    return num


print(return_number(5))