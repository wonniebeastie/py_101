# Consider these two simple functions:
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

# What will the following function invocation return?
bar(foo())


# MY SOLUTION
print(bar(foo()))

# foo() => "yes"
# "yes" passed to bar()
# (foo() or "no") => "yes" or "no" => "yes"
# False and "yes"
# False

# This returns:
# ```
# False
# ```

# When the `bar()` function is called on line 9, it calls the `foo()`
# function without any arguments. The paramter for `foo()` has a 
# default value, so it does not result in an exception being raised.
# Instead, it returns `"yes"`, which in turn gets passed as an 
# argument to the `bar()` function.

# Since the order of precedence rules state that expressions inside
# parenthesis have the highest priority, it's the expressions inside
# `(param == "no") and (foo() or "no")` that gets evaluated first.

# Since `param`'s value is NOT `"no"`, it returns `False`.
# `foo()` returns "yes" so `"yes" or "no"` returns "yes", because of
# short circuit evaluation - which is when the evaluation of a logical
# expression is stopped as soon as the overall truthiness can be 
# determined. The value that was evaluated last is returned, which is
# `"yes"`.

# Finally, `False` and `"yes"` returns `False`, again because of short
# circuit evaluation.