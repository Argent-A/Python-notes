'''This script details how to use exception handling'''


# instead of allowing an error to interrupt the process of our script we can utilize
# exception handling to anticipate any errors and handle them accordingly

numerator = 560**105

# a simple example: when performing arithmetic operations we can have the following errors
# 1.) user did not enter an integer/float/numeric value
# 2.) user is dividing by 0
# 3.) operation results in a number that is too large

denominator = input("enter any number")

while True:
    try:
        result = float(numerator/float(denominator))
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except OverflowError:
        print("The number outputted is too large.")
    except NameError:
        print("Confirm you are using a numeric value and not a string")
    except Exception as e: # this will catch anything that we have not specified as an error
        print(e)
    else:
        print(f"your value is: {str(result)}")
    finally:
        prompt = input("enter another denominator otherwise enter `no`")
        if prompt.upper() == "NO":
            break

'''How this works:
try will attempt to run the initial code, if there is no issue with this code then we jump straight to
else and finally

if the try block fails, the program will ananlyze if the exception falls into any of the specified blocks
if it does, it will do as instructed within the specified block and the code will not interrupt

The finally block is useful for actions that should always happen, such as closing the connection of a file
'''
