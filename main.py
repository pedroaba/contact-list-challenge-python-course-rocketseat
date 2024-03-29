from models.contact import Contact
from models.contact_list import ContactList


def print_menu():
    separators = '=' * 10
    print(f"{separators}Contact List{separators}")

    print("Opções:")
    print("[1] Adicionar contato")
    print("[2] Listar contatos")
    print("[3] Editar contato")
    print("[4] Marcar/Desmarcar contato como favorito")
    print("[5] Visualizar lista de contatos favoritos")
    print("[6] Apagar contato")
    print("[7] Sair")


def get_user_option() -> str | None:
    option = input("Escolha uma das opções acima: ")
    allowed_options = ["1", "2", "3", "4", "5", "6", "7"]

    if option not in allowed_options:
        print("Opção inválida, por favor digite uma opção válida!!")
        return None
    return option


def main(contact_list_manager: ContactList) -> None:
    while True:
        print_menu()

        option = get_user_option()
        if option is None:
            continue

        match option:
            case "1":
                name = input("Digite o nome: ")
                email = input("Digite o email: ")
                phone = input("Digite o telefone: ")

                contact = Contact(name, email, phone)
                contact_list_manager.add(contact)
            case "2":
                contact_list_manager.print_contacts()
            case "3":
                email = input("Digite o email do contato: ")
                contact = contact_list_manager.find_by_email(email)

                if contact is None:
                    print("Não foi possível encontrar o contato com o email passado!!")
                    continue

                print("Caso deixe o valor em brando ele não será editado!!")
                name = input("Digite o nome: ")
                email = input("Digite o email: ")
                phone = input("Digite o telefone: ")

                contact.name = name
                contact.email = email
                contact.phone = phone

                contact_list_manager.update_contact(contact)
            case "4":
                email = input("Digite o email do contato que deseja marcar/desmarcar como favorito: ")
                contact = contact_list_manager.find_by_email(email)

                if contact is None:
                    print("Não foi possível encontrar o contato com o email passado!!")
                    continue

                option_to_show = "marcar" if contact.is_favorite else "desmarcar"
                does_mark_contact_as_favorite = input(f"Deseja {option_to_show} contato como favorito? (S/n) ")

                contact.is_favorite = does_mark_contact_as_favorite.lower() == "s"
                contact_list_manager.update_contact(contact)
            case "5":
                contact_list_manager.print_favorites_contacts()
            case "6":
                email = input("Digite o email do contato que deseja apagar: ")
                contact = contact_list_manager.find_by_email(email)

                if contact is None:
                    print("Não foi possível encontrar o contato com o email passado!!")
                    continue

                contact_list_manager.delete_contact_by_email(email)
            case "7":
                print("Fechando sistema, tchau tchau!")
                exit(0)


if __name__ == "__main__":
    contact_list = ContactList()

    main(contact_list)
