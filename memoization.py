def my_function(arg1, arg2):
  if (arg1, arg2) in memo:
    return memo[(arg1, arg2)]
  else:
    result = arg1 * arg2
    memo[(arg1, arg2)] = result
    return result

memo = {}
print(my_function(1, 2))
print(my_function(1, 2))
