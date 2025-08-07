#This small application lets you add, delete, search new contacts.
#Add_contact asks for their name and number, a confirmation before creation and if not, makes the user repeat their input
def add_contact():
 while True:
    UserName = input("Enter your name: ")
    UserNumber = input("Enter your Number: ")

    contactInfo = {
        "Name": UserName,
        "Number": UserNumber
    }

    if not UserName.isalpha():
        print("Please use only letters in the name: ")
        continue

    if not UserNumber.isdigit():
        print("Please use only numbers for the phone number: ")
        continue



    print(contactInfo)

    userConfirmation = input( 'Is information correct?, respond with "Yes" or "No: ')

    if userConfirmation.lower() in ("yes", "y"):
        print(" Thanks! Information saved")
        return contactInfo


    elif userConfirmation.lower() in ("no", "n"):
        print(" Let's try again . \n")


    else:
        print(' Please type "Yes" or "No": \n')

contacts = [
     {"Name": "Alice", "Number": "9869998881"},
     {"Name": "John", "Number": "9869998882"},
     {"Name": "Barb", "Number": "9869998883"},

]

def delete_contact():
    name = input("Enter the name of the contact  you want to delete: ")
    for c in contacts:
        if c["Name"].lower() = name.lower()

def showContact():
    if not contacts:
        print("📭 Contact list is empty.\n")
    else:
        for contact in contacts:
            print(f"{contact['Name']} {contact['Number']}")

#contact works as the "database" although it has no real save function after restarting the program

def searchContact():
    while True:
        lookupName = input("what is the name of the contact you are searching for?: ")
        found = False
        for contact in contacts:
            if contact["Name"].lower() == lookupName.lower():
                print(f"{contact['Name']}: {contact['Number']}")
                found = True
                break

        if not found:
            print("❌ Contact not found.")
            again = input("Try again? (yes/no): ").lower()
            if again != "yes":
                break  # only break if they don't want to try again
        # and outside this if-block:
        else:
            break  # found the contact, no need to search again

#Menu inputs
while True:
    print("\n Contact app menu:")
    print("1 Add contacts")
    print("2 Search Contacts")
    print("3 Delete contacts")
    print("4 Show contacts")
    print("5 Exit")

# The options after asking for an input which will lead to a function being executed. Although I suppose I could put it in a def and keep it cleaner..
    choice = input("Choose an input (1-5): ")

    if choice == "1":
        contact = add_contact()
        contacts.append(contact)


    elif choice == "2":
        searchContact()



    elif choice == "3":
        deleteRequest = input("Which contact do you want to delete, write their name").lower()



    elif choice == "4":
        print(showContact())


    elif choice == "5":
        break

    else:
        break

