"""
Breakpoint structs provides as to debug our code.

c -> continue execution
q -> quit the debugger/execution
n -> step to next line within the same function
s -> step to next line in this function or a called function
"""

def debugger(a, b):
    breakpoint()
    result = a / b
    return result
  
print(debugger(5, 0))