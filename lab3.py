"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contacts
class Contact:
    number_contacts = 0
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
     
        Contact.number_contacts += 1
   
    def check_email(self, email):
        if "@" in self.email:
            return f"{self.name}'s Email Contains @"

        
    def __str__(self):

        return f"Name: {self.name} \nEmail: {self.email} \nPhone Number: {self.phone_number}\n"
        
    @classmethod
    def get_contact_count(cls):
        return cls.number_contacts

Contact1 = Contact("Bob",111,"Bob@mail")
Contact2 = Contact("Rod",222,"Rod@mail")
print(Contact1.check_email("email"))
print(f" Total Contacts: {Contact.get_contact_count()}")