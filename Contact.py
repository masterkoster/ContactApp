#This small application lets you add, delete, search new contacts.

import json


#oads json file from contacts.json and saves it into the same file
def load_contact():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts
contacts = []
load_contact()

def save_contact():
    with open ("contacts.json", "w") as f:
        json.dump(contacts, f)




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

# if else statement confirmations
    userConfirmation = input( 'Is information correct?, respond with "Yes" or "No: ')

    if userConfirmation.lower() in ("yes", "y"):
        print(" Thanks! Information saved")
        save_contact()
        return contactInfo


    elif userConfirmation.lower() in ("no", "n"):
        print(" Let's try again . \n")


    else:
        print(' Please type "Yes" or "No": \n')






#delete function that asks for an input an then looks through the contact list, then proceeds to delete thn and save it in the json file
def delete_contact():
    name = input("Enter the name of the contact  you want to delete: ")
    for c in contacts:
        if c["Name"].lower() == name.lower():
            contacts.remove(c)
            print(f"{name} has been removed")
            save_contact()
            return
    print("Contact not found.")
save_contact()
#Searches for the name saved in input
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
        save_contact()


    elif choice == "2":
        searchContact()



    elif choice == "3":
        delete_contact()
        save_contact()



    elif choice == "4":
        print(showContact())


    elif choice == "5":
        break

    else:
        break

