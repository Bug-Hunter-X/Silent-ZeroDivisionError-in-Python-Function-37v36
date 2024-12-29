def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct handling of a == 0
    elif b == 0:
        return a  # Correct handling of b == 0
    else:
        return a / b

result = function_with_uncommon_error(0, 0)  #This will return 0 correctly
print(result) 

result = function_with_uncommon_error(10, 0) #This will return 10 correctly
print(result) 

result = function_with_uncommon_error(0, 10) #This will return 10 correctly
print(result)

result = function_with_uncommon_error(10, 5)  #This will return 2.0 correctly
print(result)