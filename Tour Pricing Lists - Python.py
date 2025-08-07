"""
Programmer/s:  Jayson Justin C. Cabus , John Kevin R. De Chavez and Anne Kirsten V. Barbon
Purpose: allows a user to input and validate tour information,
calculate the gross total price and final price with discounts,
and view a summary of all the tours with the tour number, start date,
destination, number of travelers,gross total price, and final price for each tour.
The input loop continues until the user inputs the terminate value.
Language: Python 3
Date: Jan 05, 2023
"""

def get_destination_info():
    destinations = ['Chicago', 'Boston', 'Miami', 'San Francisco']
    prices = [300.00, 480.00, 1050.00, 1300.00]
    return destinations, prices

def display_destination_menu(destinations, prices):
    print()
    print("-" * 57)
    print("""   Code          Destination          Price per Person($)""")
    print("-" * 57)
    for i in range(len(destinations)):
        print(f"  {i+1:>3} {destinations[i]:>20} {prices[i]:>24.2f}")
    print()
    
def get_tour_data(tour_number, destinations, prices):
    #prompt and verify that the month, day, year, and destination code are valid
    while True:
        try:
            month = int(input("Enter month (1-12): "))
            if not (1 <= month <= 12):
                print("Invalid month.")
                continue
        except ValueError:
            print("Invalid input. Please enter month again.")
            continue
        break
    
    while True:   
        try:
            day = int(input("Enter day (1-31): "))
            if not (1 <= day <= 31):
                print("Invalid day.")
                continue
        except ValueError:
            print("Invalid input. Please enter day again.")
            continue
        break
    
    if month < 10:
        month = "0" + str(day)
    if day < 10:
        day = "0" + str(day)
    
    while True:
        try:
            year = int(input("Enter year (only years within 2023-2025 are accepted): "))
            if year < 2023 or year > 2025:
                print("Invalid year. Enter year again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break
    
    
    while True:
        try:
            num_travelers = int(input("Enter number of travelers: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    while True:
        destination_code = input("Enter destination code ('1', '2', '3', '4'): ")
        if destination_code not in ['1', '2', '3', '4']:
            print("Invalid destination code")
            continue
        break

    # calculate gross total price and price after discount
    tour_price = prices[int(destination_code)-1]
    gross_total_price = int(num_travelers) * tour_price
    discount = 0
    if int(num_travelers) >= 51:
        discount = 300
    elif int(num_travelers) >= 21:
        discount = 200
    elif int(num_travelers) >= 13:
        discount = 125
    elif int(num_travelers) >= 6:
        discount = 75
    else:
        discount = 0
    final_price = gross_total_price - (num_travelers) * (discount)

    # store tour data
    tour_data.append([tour_number, f"{month}/{day}/{year}", destination_code, destinations[int(destination_code)-1], num_travelers, gross_total_price, final_price])
    return tour_data
  
def output_tour_data(tour_data):
    print("-" * 110)
    print(f"{'Tour Number':<16} {'Start Date':<16} {'Destination':<16} {'# Travelers':<16} {'Gross Total Price':>17} {'Final Price':>17}")
    print("-" * 110)
    for tour in tour_data:
        print(f"{tour[0]:>6} {tour[1]:>20} {tour[3]:>18} {tour[4]:>9} {tour[5]:>18.2f}$ {tour[6]:>22.2f}$")
    print("-" * 110)

#main logic
tour_data = []
tour_numbers = []

while True:
    destinations, prices = get_destination_info()
    display_destination_menu(destinations, prices)
    while True:
        tour_number = input('Enter tour number.\nAccepts numbers from 0 to 999 only. Enter "0" to quit: ')
        tour_number = int(tour_number)
        if tour_number < 10:
            tour_number = "00" + str(tour_number)
        elif tour_number < 100:
            tour_number = "0" + str(tour_number)
        if tour_number in tour_numbers:
            print("Tour number already exists. Please enter a different tour number.")
            print()
            continue
        elif int(tour_number) > 999 or int(tour_number) < 0:
            print("Invalid tour number. Please enter a number again.")
            continue
        else:
            break
    if tour_number == "000":
        break
    tour_numbers.append(tour_number)
    get_tour_data(tour_number, destinations, prices)
print()
output_tour_data(tour_data)









