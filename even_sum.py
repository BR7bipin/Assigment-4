# Main Function
def main():
    # Get a positive number from the user input
    n = abs(int(input("Enter a positive number: ")))

    # Display the value of the sum_of_evens function
    print(f"Total sum of even numbers from range 1 to {n}:", sum_of_evens(n))

# sum_of_evens function
# @params n: range
# This function returns the sum of all even numbers between 1 to n
def sum_of_evens(n):
    # Initial result value
    res = 0
    # for loop that iterates variable i from range 1 to n + 1
    for i in range(1, n+1):
        # check if i is an even number
        if i % 2 == 0:
            res += i    # res = res + i
    
    return res  # return final sum result

main() # Execute the main function
