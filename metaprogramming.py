def my_meta_function(template_string, **kwargs):
  result = template_string.format(**kwargs)
  return result

print(my_meta_function("Hello, {name}!", name="Bard"))
