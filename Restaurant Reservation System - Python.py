"""
Programmer/s: John Kevin R. De Chavez, Jayson Justin C. Cabus and Anne Kirsten V. Barbon
Purpose: for a restaurant reservation system. The system has functions to view, make, delete,
and generate reports for reservations. The user can input their name, the date and time they want to reserve,
and the number of adults and children in their party. The system will store this information in arrays for future reference.
The system has error checkers for invalid inputs, such as incorrect dates or times.
The system can also generate reports of the number of reservations made, the number of adults and children in each reservation,
and the subtotal of all reservations. The system has an exit function to close the program.
Language: python 3
Date: Jan 05, 2023
"""

#Arrays to store user input
reservation_num = []
dates = []
times = []
names = []
adult_count = []
children_count = []
subtotal = []

#modules to be called
def menu():
    print('''
RESTAURANT RESERVATION SYSTEM
    
System Menu

    a. View all Reservations
    b. Make Reservation
    c. Delete Reservation
    d. Generate Report
    e. Exit
    ''')

def reservations(reservation_num, dates, times, names, adult_count, children_count):
    if len(reservation_num) < 1:
        print("There are no reservations made right now to display.")
    else:
        print()
        print("#     Date           Time               Name                 Adults            Children")
        for res in range(0, len(reservation_num)):
            print(f"{reservation_num[res]} {dates[res]:>4} {times[res]:>13} {names[res]:>24} {adult_count[res]:>12} {children_count[res]:>18}")

def make_reservation():
    #input prompt for name
    print()
    name = str(input("Please enter your name to make a reservation:\n"))
    
    #input prompt for date with error checker
    print()
    while True:
        try:
            date, day, year = input("Please enter the date you want to reserve.\n(Use this format: Month Day Year, e.g., Jan 05 2023. Use only the first three letters of the month.)\nOnly dates within year 2023 are accepted:\n").split()
            break
        except ValueError:
            print("Invalid input. Please enter a valid date.")
            print()
    date = date.lower()
    day = int(day)
    months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
    while date not in months or date == "" or day > 31 or day < 1 or year != "2023":
        print("Invalid input. Please enter a valid date.")
        print()
        while True:
            try:
                date, day, year = input("Please enter the date you want to reserve.\n(Use this format: Month Day Year, e.g., Jan 05 2023. Use only the first three letters of the month.)\nOnly dates within year 2023 are accepted:\n").split()
                break
            except ValueError:
                print("Invalid input. Please enter a valid date.")
                print()
        date = date.lower()
        day = int(day)
    if day < 10:
        day = "0" + str(day)
    else: 
        day = str(day)
    date = date.capitalize()
    date = date + " " + day + " " + year
    
    #input prompt for time with error checker
    #for determining am or pm
    print()
    timeOfDay = input('Which time of the day will you visit? (Input "am" or "pm" only)\n').lower()
    timeList = ["am","pm"]
    while timeOfDay not in timeList or timeOfDay == "":
        print("Invalid option. Please select from the options only.")
        print()
        timeOfDay = input('Which time of the day will you visit? (Input "am" or "pm" only)\n').lower()
    #for exact time of reservation
    while True:
        try:
            time, minutes = input('Please enter the time that you want to reserve (Enter the time only, e.g., "11:00"):\n').split(":")
            if len(minutes) > 2 or minutes == "":
                print("Invalid input. Please enter a valid time.")
                print()
                continue
            break
        except TypeError:
            print("Invalid input. Please enter a valid time.")
            print()
        except ValueError:
            print("Invalid input. Please enter a valid time.")
            print()
        except Exception:
            print("Invalid input. Please enter a valid time.")
            print()

    time = int(time)
    minutes = int(minutes)
    while time > 12 or time < 1 or minutes > 59 or minutes < 0:
        print("Invalid time. Please enter a valid time.")
        print()
        while True:
            try:
                time, minutes = input('Please enter the time that you want to reserve (Enter the time only, e.g., "11:00"):\n').split(":")
                break
            except ValueError:
                print("Invalid time. Please enter a valid time.")
                print()
        time = int(time)
        minutes = int(minutes)
    if time < 10:
        time = str(time)
        time = "0" + time 
    time = str(time)
    if minutes == 0:
        minutes = str(minutes)
        minutes = "0" + minutes
    minutes = str(minutes)
    time = time + ":" + minutes
    time = time + " " + timeOfDay
        
    #input prompt for no. of adults with error checker
    print()
    while True:
        try:
            adult = int(input("How many of you are adults?\n"))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    adult_fee = adult * 500
        
    #input prompt for no. of child/ren with error checker
    print()
    while True:
        try:
            child = int(input("How many of you are child/ren?\n"))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    children_fee = child * 300
    total = adult_fee + children_fee
    
    #append all inputted data into the lists
    length = len(reservation_num) + 1
    reservation_num.append(length)
    dates.append(date)
    times.append(time)
    names.append(name)
    adult_count.append(adult)
    children_count.append(child)
    subtotal.append(total)
    return name, date, time, adult, child, subtotal 

def delete_reservation():
    if len(reservation_num) == 0:
        print("There are no reservations to remove right now.")
    else:
        print()
        while True:
            try:
                delResNum = int(input('Enter the number of the reservation that you want to delete (Type "0" to return to main menu):\n'))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                print()
            if delResNum > len(reservation_num) or delResNum < 0:
                print("Invalid reservation number. Please enter a valid number.")
                print()
                continue
            if delResNum == 0:
                break
            break
        if delResNum == 0:
            return
        else:
            reservation_num.remove(reservation_num[delResNum-1])
            counter  = delResNum-1
            for i in range(delResNum, len(reservation_num)+1):
                reservation_num[counter] -= 1
                counter += 1
            dates.remove(dates[delResNum - 1])
            times.remove(times[delResNum - 1])
            names.remove(names[delResNum - 1])
            adult_count.remove(adult_count[delResNum - 1])
            children_count.remove(children_count[delResNum - 1])
            print(f"Reservation no. {delResNum} is deleted successfully.")

def generate_report(reservation_num, dates, times, names, adult_count, children_count, subtotal):
    total_adults = sum(adult_count)
    total_children = sum(children_count)
    grand_total = sum(subtotal)
    if len(reservation_num) < 1:
        print("There are no reservations made to display.")
    else:
        print()
        print("#     Date           Time               Name                 Adults            Children            Subtotal")
        for res in range(0, len(reservation_num)):
            print(f"{reservation_num[res]} {dates[res]:>4} {times[res]:>13} {names[res]:>24} {adult_count[res]:>12} {children_count[res]:>18} {subtotal[res]:>22.2f}")
        print()
        print(f"Total number of Adults: {total_adults}")
        print(f"Total number of Kids: {total_children}")
        print(f"Grand Total: PHP {grand_total:.2f}")

def exit():
    print("Thank you for using the program!")
    
#Main program run
menu()
choice = input("Select an action from the menu (only the letter of your choice): ").lower()
while choice != "e":
    # Call the corresponding function based on the user's selection
    if choice == "a":
        reservations(reservation_num, dates, times, names, adult_count, children_count)
    elif choice == "b":
        make_reservation()
    elif choice == "c":
        delete_reservation()
    elif choice == "d":
        generate_report(reservation_num, dates, times, names, adult_count, children_count, subtotal)
    else:
        print("Invalid choice. Please select a valid option from the menu.")
    menu()
    choice = input("Select an action from the menu (only the letter of your choice): ").lower()
exit()










