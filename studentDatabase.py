# Create 3 list with student info: name, hometown, favorite food
# Display welcome message with menu options: 1) display list of students, 2) search database 3) Exit
# Ask user to select menu option
    # If 1: display list of students then return to the menu
    # If 2: Provide second menu to search by either index or name
        # If 1:
            # Ask user for index number
            # Print student name via index
            # Ask for additional info category selection via numbered menu
                # If 1: print student hometown
                # If 2: print student favorite food
            # Ask user to continue or terminate loop
        # If 2:
            # Ask user for name
            # Search for and store index number of student based on name
            # Print student name based on index found
            # Ask for additional info category selection via numbered menu
                # If 1: print student hometown
                # If 2: print student favorite food
    # If 3: exit

def menu1_print_select():
    print("""
Welcome! What would you like to do?
1. Display student list
2. Search student database
3. Exit system

Enter menu choice:""")
    try:
        menu_choice = int(input())
        if 1 > menu_choice > 3:
            print("Invalid menu option! Must be a number shown in menu!")
        else:
            return menu_choice
    except:
        print("Invalid choice! Must be a number shown in menu!")
        menu1_print_select()

def info_selection(student_choice):
    print("Student {0} is {1}. What would you like to know? \n1) Hometown or 2) Favorite Food".format(student_choice, nameList[student_choice - 1]))
    info_choice = int(input())
    match info_choice:
        case 1:
            print("{0} is from {1}.".format(nameList[student_choice - 1], hometownList[student_choice - 1]))
        case 2:
            print("{0}'s favorite food is {1}.".format(nameList[student_choice - 1], foodList[student_choice - 1]))

nameList = ['John', 'James', 'Sarah', 'Mary', 'Peter']
hometownList = ['Detroit', 'Chicago', 'Toronto', 'New York', 'Boston']
foodList = ['Gyro', 'Pizza', 'Sushi', 'Mediterranean', 'Crab']

keep_going = 'y'

while keep_going == 'y':
    menu_choice = menu1_print_select()
    match menu_choice:
        case 1:
            for name in nameList:
                print("{0}. {1}".format((int(nameList.index(name)) + 1), name))
            print()
            keep_going = input("Return to main menu? (y/n) ")
        case 2:
            search_choice = int(input("Would you like to search by: 1) number (1-5) or 2) name "))
            match search_choice:
                case 1:
                    student_choice = int(input("Enter student number (1 - 5): "))
                    info_selection(student_choice)
                    keep_going = input("Return to main menu? (y/n) ")
                case 2:
                    name_search = input("Enter the name of the student you're searching for: ")
                    name_search2 = name_search.capitalize()
                    valid_name = False
                    if not valid_name:
                        try:
                            selected_index = int(nameList.index(name_search2.capitalize()))
                            valid_name = True
                        except:
                            print("Name not found! Try again!")
                            break
                    student_choice = selected_index + 1
                    info_selection(student_choice)
                    keep_going = input("Return to main menu? (y/n) ")
        case 3:
                keep_going = 'n'
