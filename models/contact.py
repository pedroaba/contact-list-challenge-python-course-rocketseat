import uuid


class Contact:
    def __init__(self, name: str, email: str, phone: str) -> None:
        self._id = str(uuid.uuid4())
        self._name = name
        self._email = email
        self._phone = phone
        self._is_favorite = False

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            return

        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if not value:
            return

        self._email = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        if not value:
            return

        self._phone = value

    @property
    def id(self) -> str:
        return self._id

    @property
    def is_favorite(self) -> bool:
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, value: bool) -> None:
        self._is_favorite = value

    def __str__(self) -> str:
        return f'Nome: {self.name}, Email: {self.email}, Telefone: {self.phone}, Contato Favorito: {self._is_favorite}'
