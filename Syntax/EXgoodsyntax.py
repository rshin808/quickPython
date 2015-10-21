# Global Variables
test_array = [1, 2, 3, 4]

def function1():
    """This function inverses the global test_array. 
    """
    # Declare the global
    global test_array

    # Inverse the test_array
    test_array = test_array[::-1]

# Array before function1
print test_array

# Call function1
function1()
print test_array
