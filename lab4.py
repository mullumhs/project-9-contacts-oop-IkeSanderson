"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Implement the ContactManager class and perform CRUD operations.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Import the ContactManager class here.

from contact_manager import ContactManager
CM = ContactManager()
# 2. Go to the 'contact_manager.py' file and implement the TODO in the display_contacts method.



# 3. Create two contacts using the ContactManager.

CM.add_contact("Bob",111,"Bob@mail")
CM.add_contact("Rod",222,"Rod@mail")


# 4. Display all contacts.

CM.display_contacts()

# 5. Update the email address of one contact.

CM.update_contact("Bob", new_email= "Bobble@mail")

# 6. Remove one of the contacts.

CM.remove_contact("Rod")

# 7. Display all contacts again.

CM.display_contacts()
