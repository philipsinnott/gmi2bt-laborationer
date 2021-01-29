import json, csv, pprint

# READ .JSON FILE #
def read_file_json(file_name='swag.json'):
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as json_file:
            content = json.load(json_file)
            return content
    except FileNotFoundError:
        print(f'We could not find the file {json_file}.')
    except FileExistsError:
        print(f'The file {json_file} already exists.')

# WRITE TO .JSON FILE #
def write_to_file_json(data):
    try:
        with open('swag.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print(f'We could not find the file {json_file}.')

# READ .CSV FILE#
def read_file_csv(file_name='labb2-personer.csv'):
    rows = []
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as csv_file:
            #reader = csv.reader(csv_file, delimiter=';')
            #next(reader)
            for row in csv_file:
                row = row.rstrip('\n').split(';')
                students = {'user': row[0], 'fname': row[1], 'lname': row[2], 'email': row[3]}
                rows.append(students)
            print('File has been read...\nGoing back to main menu.')
            print()
            return rows
    except FileNotFoundError:
        print(f'We could not find the file {csv_file}.')
    except FileExistsError:
        print(f'The file {csv_file} already exists.')

# DELETE STUDENT #
def delete_student(students):
    user = input('Username: ')
    i = 0
    for student in students:
        if student['user'].strip() == user.strip():
            break
        i += 1
        if i < len(students):
            students.pop(i)
            print(f'{user} has been removed from the students list!')
            write_to_file_json(students)

# ADD STUDENT #
def add_student(students):
    print('--------------------------------------')
    print('Enter information to add a new student')
    username = input('Username: ')
    first_name = input('First name: ')
    last_name = input('Last name: ')
    email = input('Email: ')
    students.append({'user': username, 'fname': first_name, 'lname': last_name, 'email': email})
    print(f'{username} has been added to the students list!')
    print('--------------------------------------')
    print()
    write_to_file_json(students)

# SAVE FILE #
def save_file(students):
    write_to_file_json(students)
    print('The file has been saved.')

# SHOW STUDENTS #
def show_students(students):
    print('--------------------------------------')
    for student in students:
        pprint.pprint(student, indent=4)
    print('--------------------------------------')

# MENU #
students = read_file_json()
def menu():
    while True:
        choice = input("[1]: Read original file (labb2-personer.csv)\n"
                       "[2]: Show json-data\n"
                       "[3]: Add a person\n"
                       "[4]: Remove a person\n"
                       "[5]: Save file\n"
                       "[6]: Exit\n"
                       "Choose what you want to do: ")
        if choice == "1":
            students = read_file_csv()
            #input("Press any key to continue to the main menu.")
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            add_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            save_file(students)
        elif choice == "6":
            print("Au revoir.")
            break
        else:
            print("Invalid input, please choose a valid option (1-3).")