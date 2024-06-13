"""
ejercicio

"""

# pila/ stack (LIFO)

stack = []
#push

stack.append("3")
stack.append("2")
stack.append("1")

#pop
stack_item = stack[len(stack)-1]
del stack[len(stack)-1]
print (stack_item)
print (stack.pop())
print (stack)
