from pathlib import Path
import re


contacts = dict()
phonebook_path = Path(Path.cwd() / 'my_phonebook.txt')
try:
    with open(phonebook_path, 'r') as book:
        if len(contacts) < 1:
            while True:
                line = book.readline()
                if not line:
                    break
                else:
                    line = line.strip().split()
                    contacts[line[0]] = line[1]
except Exception as e:
    print(f'Can`t read file with contacts: {e}.\nProceed in live-mode')


def contacts_update():
    try:
        with open(phonebook_path, 'w') as book:
            for name, phone_number in contacts.items():
                book.write(f"{name} {phone_number}\n")
    except Exception as e:
        print(f'Can`t update file with contacts: {e}.\nProceed in live-mode')

def add_contact(*args):
    is_exist, name, phone_number = args_processing(*args)
    
    if is_exist:
        contacts[name] = phone_number
        print(f'Contact {name} added')
        contacts_update()
    else:
        print(f'Contact {name} was not added, try again, please.')
        


def change_contact(*args):
    if contacts is None or len(contacts) == 0:
        print('Phonebook is empty')
    is_exist, name, phone_number = args_processing(*args)
    if phone_number is None:
        print('Incorrect phone number')
    elif name in contacts:
        contacts[name] = phone_number
        print(f'Contact {name} was updated by phone number {contacts.get(name)}')
        contacts_update()
    else:
        print(f'Contact {name} not found')




def show_contact(*args):
    if contacts is None or len(contacts) == 0:
        print('Phonebook is empty')
        return
    if len(args) == 0:
        name = get_name()
    else:
        name = args[0] 
    if check_contact(name):
        print(f'{name}: {contacts.get(name)}')
    else:
        print(f'Contact {name} not found')

def show_all():
    print(contacts)


def args_processing(*args) -> list[bool, str, str]:
    info = args
    name, phone_number = "", ""
    if info is None or len(info) == 0:
        name = get_name()
        phone_number = get_phone_number(None)
    elif len(info) == 1:
        if re.match("[0-9]", info[0]):
            print(f"Incorrect contact name {info[0]}, contact wasn`t added")
            return False, None, None
        else:
            phone_number = get_phone_number(None)
            name = info[0]
    else:
        if re.match("[0-9]", info[-1]):
            phone_number = info[-1]
            name = ""
            for item in info:
                if item != phone_number:
                    name += item + " "
            phone_number = get_phone_number(phone_number)
        else:
            print(f"Incorrect contact data {info}, contact wasn`t added")
            return False, None, None
    return name and phone_number, name, phone_number


def get_name() -> str:
    while True:
        name = input('Enter contact`s name:  ')
        if name:
            return name 


def get_phone_number(number: str) -> str:
    while True:
        if number is None:
            number = input('Enter phone number: ')
        if number is not  None:
            number = re.sub("[^0-9]", "", number)

            # Suffix correction
            if len(number) == 12:
                return "+" + number
            if len(number) == 11:
                return "+3" + number
            if len(number) == 10:
                return "+38" + number
            return None


def check_contact(name: str) -> bool:
    return  (name is not None and name in contacts.keys())