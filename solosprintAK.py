import csv
import os

#where data is stored
active_users = []
disabled_users = []
FileName = "user_data.csv"

#loading data from user_data.csv for data persistence stretch goal
def load_from_csv(): 
    if os.path.exists(FileName):
        with open(FileName, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = {"username": row['username'], "password": row['password']}
                if row['status'] == 'Active':
                    active_users.append(user)
                else:
                    disabled_users.append(user)
        print("Data loaded successfully.")
    else:
        print("No Data found, please start adding data.")

#saving data to my file user_data.csv
def save_to_csv():
    """Stretch Goal: Persist users to CSV"""
    with open(FileName, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password", "status"])
        writer.writeheader()
        for user in active_users:
            writer.writerow({**user, "status": "Active"})
        for user in disabled_users:
            writer.writerow({**user, "status": "Disabled"})
    print(f"Data saved to {FileName}")

#choice 1: adding users function
def add_user():
    username = input("Enter new username: ")
    password = input("Enter password: ")
    new_user = {"username": username, "password": password}
    active_users.append(new_user)
    print(f"User {username} added successfully.")

#choice 2: view users function
def view_users():
    print("Active Users")
    for user in active_users:
        print(f"User: {user['username']}")
    
    print("Disabled Users")
    for user in disabled_users:
        print(f"User: {user['username']}")

#choice 3: enable/disable users
def toggle_user_status():
    choice = input("Do you want to disable or enable a user? type disable / enable").lower()
    username = input("Enter username: ")
    
    if choice == 'disable':
        for user in active_users:
            if user['username'] == username:
                active_users.remove(user)
                disabled_users.append(user)
                print(f"{username} has been disabled.")
                return
    elif choice == 'enable':
        for user in disabled_users:
            if user['username'] == username:
                disabled_users.remove(user)
                active_users.append(user)
                print(f"{username} has been enabled.")
                return

#choice 4 test login
def test_login():
    """Menu Item 4: Verify credentials"""
    name = input("Username: ")
    pw = input("Password: ")
    
    # Check both lists
    for user in (active_users + disabled_users):
        if user['username'] == name and user['password'] == pw:
            print("ACCESS GRANTED")
            return
    print("ACCESS DENIED")

#main menu
def main_menu():
    while True:
        print("User Management System")
        print("1. Add User")
        print("2. View Users")
        print("3. Enable/Disable Users")
        print("4. Test Login")
        print("0. Save and Exit")

        choice = input("Select an option: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            view_users()
        elif choice == '3':
            toggle_user_status()
        elif choice == '4':
            test_login()
        elif choice == '0':
            save_to_csv()
            print("Exiting App")
            break
        else:
            print("Invalid choice! Try again!")

#loads stored data for data persistence
if __name__ == "__main__":
    load_from_csv()
    main_menu()

