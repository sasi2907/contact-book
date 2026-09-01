again_choices = ["yes", "y", "n", "no"]

def create_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = {
    "name": name,
    "phone": phone,
    "email": email
    }
    return contact

def add_contact():
    adding_contact = True
    while adding_contact:

        contact = create_contact()
        contacts.append(contact)

        again_checking = True
        while again_checking:
            again = input("do you want to add another contact (y/n)? ")
            again = again.lower()
            if again in again_choices:
                again_checking = False

                if again == "n" or again =="no":
                    adding_contact = False
                else:
                    print("Enter a valid option(y/n)!")

def view_contacts():
    print("================")
    print("    CONTACTS    ")
    print("================")
    
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"email: {contact['email']}")
        print("-----------------------------")


def search_contact():
    search_again = True
    while search_again:
        search_name = input("Enter a name to search: ")
        search_name  = search_name.lower()

        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name:
                print("contact found!")
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                search_again = False

                found = True

            break

        if not found:
            print("contact not found.")

def update_contact():
    search_name = input("Enter the name of the contact to update: ")
    search_name = search_name.lower()

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name:
            found = True

            print("Contact found!")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Phone")
            print("3. Email")

            choice = input("Enter your choice: ")

            if choice == "1":
                contact["name"] = input("Enter new name: ")

            elif choice == "2":
                contact["phone"] = input("Enter new phone: ")

            elif choice == "3":
                contact["email"] = input("Enter new email: ")

            else:
                print("Invalid choice.")

            break

    if not found:
        print("Contact not found.")


def delete_contact():
    search_name = input("Enter the name of the contact to delete: ")
    search_name = search_name.lower()

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name:
            found = True

            print("Contact found!")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

            confirm = input("Are you sure you want to delete this contact? (y/n): ")
            confirm = confirm.lower()

            if confirm == "y" or confirm == "yes":
                contacts.remove(contact)
                print("Contact deleted successfully.")
            else:
                print("Contact was not deleted.")

            break

    if not found:
        print("Contact not found.")

contacts = []

while True:
    print("==============================")
    print("         CONTACT BOOK")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please choose 1-6.")