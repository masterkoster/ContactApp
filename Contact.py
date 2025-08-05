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
    contact = add_contact()
    contacts.append(contact)

    cont = input("Add another contact? (yes/no): ").lower()

    if cont != "yes":
        break

print("\nAll contacts:")
for c in contacts:
    print(f"{c['Name']}: {c['Number']}")