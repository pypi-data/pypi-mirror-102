def say_hello(name=None):
    if name is None:
        return "Hello, World!" * 5
    else:
        return f"Hello, {name}!" * 5