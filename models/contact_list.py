from models.contact import Contact


class ContactList:
    def __init__(self) -> None:
        self._contacts: list[Contact] = []

    def add(self, contact: Contact) -> None:
        self._contacts.append(contact)

    def print_contacts(self) -> None:
        if len(self._contacts) == 0:
            print("Lista de contatos vazia!")
            return

        for index, contact in enumerate(self._contacts):
            print(f"{index + 1}. {contact}")

    def print_favorites_contacts(self) -> None:
        favorites_contacts: list[Contact] = list(
            filter(lambda c: c.is_favorite, self._contacts)
        )

        if len(favorites_contacts) == 0:
            print("Lista de contatos favoritos vazia!")
            return

        for index, contact in enumerate(favorites_contacts):
            print(f"{index + 1}. {contact}")

    def find_by_email(self, email: str) -> Contact | None:
        for contact in self._contacts:
            if contact.email == email:
                return contact

    def update_contact(self, updated_contact: Contact):
        contact_index = -1
        for index, contact in enumerate(self._contacts):
            if contact.id == updated_contact.id:
                contact_index = index

        if contact_index != -1:
            self._contacts[contact_index] = updated_contact

    def delete_contact_by_email(self, email: str):
        self._contacts = list(
            filter(lambda c: c.email != email, self._contacts)
        )
