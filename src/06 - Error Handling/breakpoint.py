def debugger(a, b):
    breakpoint()
    result = a / b
    return result
  
print(debugger(5, 0))

"""

c -> continue execution
q -> quit the debugger/execution
n -> step to next line within the same function
s -> step to next line in this function or a called function

"""