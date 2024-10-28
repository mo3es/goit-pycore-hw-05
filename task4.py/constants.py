from colorama import Fore

pattern_quit = {"exit", 'quit', 'close', 'вихід', "вийти", 'stop', 'закрити'}
pattern_add = {'add', 'plus', 'append', 'adding', 'додати', "плюс"}
pattern_change = {'change', 'змінити', 'замінити'}
pattern_show = {'phone', 'show', 'look', 'find', 'give', 'contact', 'номер', 'покажи','показати', 'знайти', 'знайди', 'дай', 'контакт'}
pattern_all = {'all', 'show-all', 'print-all', 'print', 'phone-book', 'contacts', 'list', 'усі', 'всі', 'друк', 'друкуй', 'роздрукуй', 'список', 'перелік', 'телефонна-книга','контакти'}
pattern_hello = {'hello', 'hi', 'привіт'}


USAGE = f"""
    Usage:
    # {Fore.BLUE}For quit - {Fore.GREEN}"exit", 'quit', 'close', 'вихід', "вийти", 'stop', 'закрити'
    # {Fore.BLUE}For adding contact - {Fore.GREEN}<'add', 'plus', 'append', 'adding', 'додати', "плюс"> {Fore.LIGHTGREEN_EX}[optional - ' ' <contact name> ' ' <contact number>]
    # {Fore.BLUE}For contact changing -  {Fore.GREEN}<'change', 'змінити', 'замінити'> {Fore.LIGHTGREEN_EX}[optional -  ' ' <contact name> ' ' <new contact number>]
    # {Fore.BLUE}For getting contact info - {Fore.GREEN}<'phone', 'show', 'look', 'find', 'give', 'contact', 'номер', 'покажи','показати', 'знайти', 'знайди', 'дай', 'контакт'> {Fore.LIGHTGREEN_EX}[optional - ' ' <contact name>]
    # {Fore.BLUE}For getting all contacts - {Fore.GREEN}'all', 'show-all', 'print-all', 'print', 'phone-book', 'contacts', 'list', 'усі', 'всі', 'друк', 'друкуй', 'роздрукуй', 'список', 'перелік', 'телефонна-книга','контакти'{Fore.RESET}
"""

INCORRECT_MESSAGE = f"{Fore.RED}Sorry, but I don`t recognize your input, try again, please{Fore.RESET}"