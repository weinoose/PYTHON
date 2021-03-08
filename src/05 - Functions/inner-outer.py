def outer(number):

    def inner(power):

        return number ** power

    return inner

print(outer(3)(2))