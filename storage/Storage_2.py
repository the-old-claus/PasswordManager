import os
import pickle
import pandas as pd

def save_password(pickle_file_path, website, username, password):
    data = {'Website': website, 'Username': username, 'Password': password}

    try:
        with open(pickle_file_path, 'rb') as file:
            existing_data = pickle.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(data)

    os.makedirs(os.path.dirname(pickle_file_path), exist_ok=True)

    with open(pickle_file_path, 'wb') as file:
        pickle.dump(existing_data, file)

    print(f"Password for {website} saved successfully!")

def view_passwords(pickle_file_path):
    try:
        with open(pickle_file_path, 'rb') as file:
            data = pickle.load(file)
            df = pd.DataFrame(data)
            print(df)
    except FileNotFoundError:
        print("No passwords stored yet.")

def delete_password(pickle_file_path, website):
    try:
        with open(pickle_file_path, 'rb') as file:
            existing_data = pickle.load(file)
    except FileNotFoundError:
        existing_data = []

    updated_data = [item for item in existing_data if item['Website'] != website]

    with open(pickle_file_path, 'wb') as file:
        pickle.dump(updated_data, file)

    print(f"Password for {website} deleted successfully!")

def update_password(pickle_file_path, website, new_password):
    try:
        with open(pickle_file_path, 'rb') as file:
            existing_data = pickle.load(file)
    except FileNotFoundError:
        existing_data = []

    for item in existing_data:
        if item['Website'] == website:
            item['Password'] = new_password

    with open(pickle_file_path, 'wb') as file:
        pickle.dump(existing_data, file)

    print(f"Password for {website} updated successfully!")

pickle_file_path = os.path.join('C:', 'Users', 'shres', 'OneDrive', 'Desktop', 'Py Syntax', 'Book1.pkl')

while True:
    print("\n1. Save Password")
    print("2. View Password")
    print("3. Delete Password")
    print("4. Update Password")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        website = input("Enter the website: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        save_password(pickle_file_path, website.encode('utf-8'), username.encode('utf-8'), password.encode('utf-8'))

    elif choice == '2':
        view_passwords(pickle_file_path)

    elif choice == '3':
        website_to_delete = input("Enter the website to delete: ")
        delete_password(pickle_file_path, website_to_delete)

    elif choice == '4':
        website_to_update = input("Enter the website to update: ")
        new_password = input("Enter the new password: ")
        update_password(pickle_file_path, website_to_update, new_password.encode('utf-8'))

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
