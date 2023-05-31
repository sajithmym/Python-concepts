def my_decorator(func):
  def wrapper(*args, **kwargs):
    print("Before function call")
    result = func(*args, **kwargs)
    print("After function call")
    return result
  return wrapper

@my_decorator
def my_function(arg1, arg2):
  return arg1 + arg2

print(my_function(10, 90))
