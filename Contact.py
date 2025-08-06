def add_contact():
 while True:
    UserName = input("Enter your name: ")
    UserNumber = input("Enter your Number: ")

    contactInfo = {
        "Name": UserName,
        "Number": UserNumber
    }

    print(contactInfo)

    userConfirmation = input( 'Is information correct?, respond with "Yes" or "No: ')

    if userConfirmation.lower() == "yes":
        print(" Thanks! Information saved")
        return contactInfo


    elif userConfirmation.lower() == "no":
        print(" Let's try again . \n")


    else:
        print(' Please type "Yes" or "No": \n')
contacts = []

while True:
    print("\n Contact app menu:")
    print("1.Add contacts")
    print("2 Search Contacts")
    print("3 Delete contacts")
    print("4 Show contacts")
    print("5 Exit")

    choice = input("Choose an input (1-5): ")

    if choice == "1":
        contact = add_contact()
        contacts.append(contact)


    elif choice == "2":
     while True:
        lookupName = input("what is the name of the contact you are searching for?: ")
        found = False
        for  contact in contacts:
            if contact["Name"].lower() == lookupName.lower():
                print(f"{contact['Name']}: {contact['Number']}")

        if not found:
           print("❌ Contact not found.")




    elif choice == "3":
        print("")

    elif choice == "4":
        print("")

    elif choice == "5":
        print("")






contacts = []

while True:
    contact = add_contact()
    contacts.append(contact)

    cont = input("Add another contact? (yes/no): ").lower()

    if cont != "yes":
        break

print("\nAll contacts:")
for c in contacts:
    print(f"{c['Name']}: {c['Number']}")