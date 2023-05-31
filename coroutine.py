def my_coroutine():
    while True:
        message = yield
        print(message)

coroutine = my_coroutine()
next(coroutine)  # Initialize the coroutine

coroutine.send("Hello")
coroutine.send("World")
