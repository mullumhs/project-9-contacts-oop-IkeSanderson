"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.
class Contact:
    number_contacts = 0
    def __init__(self, name, phone_number, email, contact_number):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.contact_number = contact_number
        Contact.number_contacts += 1
        


# Create at least two instances of the Contact class with different data.
Contact1 = Contact("Bob",111,"Bob@mail",1)
Contact2 = Contact("Rod",222,"Rod@mail",2)

# Write code that prints out the details of each contact you have created.
print(f"Number of Contacts: {Contact.number_contacts}")
print(f"Contact {Contact1.contact_number} - Name: {Contact1.name} - Phone Number: {Contact1.phone_number} - Email: {Contact1.email} ")
print(f"Contact {Contact2.contact_number} - Name: {Contact2.name} - Phone Number: {Contact2.phone_number} - Email: {Contact2.email} ")


