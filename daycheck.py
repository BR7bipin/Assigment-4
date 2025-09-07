def main():
    day_num = input("Enter a number between 1-7: "))
    print(day_checker(day_num))
def day_checker(day_num):
    match day_num:
        case "1": 
            return "Monday"
        case "2":
            return "Tuesday"
        case "3":
            return "Wednesday"
        case "4":
            return "Thursday"
        case "5":
            return "Friday"
        case "6":
            return "Saturday"
        case "7":
            return "Sunday"
        case _:
            return "Invalid Input" 
main()
