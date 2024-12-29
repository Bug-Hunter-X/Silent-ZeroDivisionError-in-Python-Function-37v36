def improved_function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        raise ZeroDivisionError("Both inputs cannot be zero.")  #Explicitly raise the error
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = improved_function_with_uncommon_error(0, 0)
print(result)

result = improved_function_with_uncommon_error(10, 0)
print(result) 

result = improved_function_with_uncommon_error(0, 10) 
print(result)

result = improved_function_with_uncommon_error(10, 5) 
print(result)