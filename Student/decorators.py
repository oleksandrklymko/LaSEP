def check_decorator(func):
    def wrapper_function(*args, **kwargs):
        student = args[1]
        group = args[0]
        if student in group.members:
            return func(*args, **kwargs)
        return False
    return wrapper_function
