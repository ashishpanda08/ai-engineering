# exercise:
from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    phone: int
    email: str = "name@email.com"


alex = Contact("Alex", 8987678981, "alex@random.com")
print(alex.name, alex.email, alex.phone)


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_by_name(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


book = ContactBook()

alice = Contact("Alice", "1234567890")
book.add_contact(alice)

result = book.find_by_name("Alice")
print(result.phone)  # 1234567890
