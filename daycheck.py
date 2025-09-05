# Main Function
def main():
    # Get day_num from the user input
    day_num = int(input("Enter a number between 1-7: "))
    # Display the return value of day_checker function
    print(day_checker(day_num))

# day_checker function
# @params day_num: number of the correspoding day
# returns the name of the day corresponding to the day_num, 
# otherwise returns "Invalid Input" as default
def day_checker(day_num):
    # Match case statement on day_num parameter
    match day_num:
        case 1: 
            return "Monday" # Returns 'Monday' on day_name = 1
        case 2:
            return "Tuesday" # Returns 'Tuesday' on day_name = 2
        case 3:
            return "Wednesday" # Returns 'Wednesday' on day_name = 3
        case 4:
            return "Thursday" # Returns 'Thursday' on day_name = 4
        case 5:
            return "Friday" # Returns 'Friday' on day_name = 5
        case 6:
            return "Saturday" # Returns 'Saturday' on day_name = 6
        case 7:
            return "Sunday" # Returns 'Sunday' on day_name = 7
        case _:
            return "Invalid Input" # Returns 'Invalid Input' as the default case

main()  # Run the main function
