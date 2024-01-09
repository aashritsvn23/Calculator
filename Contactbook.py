class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print(f"Contact {name} added successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\nContacts:")
            for name, phone_number in self.contacts.items():
                print(f"{name}: {phone_number}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"\nContact found - {name}: {self.contacts[name]}")
        else:
            print(f"\nContact not found for {name}.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            contact_book.add_contact(name, phone_number)

        elif choice == '2':
            contact_book.display_contacts()

        elif choice == '3':
            name = input("Enter the name to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            print("Exiting the contact book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
