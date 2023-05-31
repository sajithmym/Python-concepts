def my_function(obj):
  obj.do_something()

class MyObject:
  def do_something(self):
    print("I am doing something")

my_object = MyObject()
my_function(my_object)
