def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)

# what does the add_five return?
# The `add_five` function is a closure that captures the value of `x` from the `outer` function. When you call `add_five(3)`, it returns the result of adding 5 (the value of `x`) to 3 (the argument passed to `inner`). Therefore, `add_five(3)` returns 8.
print(add_five(3))  # Output: 8
