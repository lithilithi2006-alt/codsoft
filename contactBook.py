contacts={}
while True:
    print("\n ---CONTACT BOOK ---")
    print("1.Add Contact")
    print("2.View Contacts")
    print("3.Search Contact")
    print("4.Update Contact")
    print("5.Delete contact")
    print("6. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name]={
            "phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added successfully!")
    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            for name, details in contacts.items():
                print(f"\nName: {name}")
                print("phone:", details["phone"])
                print("Email:", details["Email"])
                print("Address:", details["Address"])

    elif choice == "3":
        search = input("Enter name to search:")
        if search in contacts:
            print(contacts[search])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to update: ")

        if name in contacts:
            contacts[name]["phone"] = input("New Phone: ")
            contacts[name]["Email"] = input("New Email: ")
            contacts[name]["Address"] = input("New Address: ")
            print("Contact updated sucessfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete:")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
            
    
                
     
