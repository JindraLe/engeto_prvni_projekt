from task_template import TEXTS

ODDELOVAC = 50 * '-'
REGISTROVANI = {'bob': '123',
                'ann': 'pass123',
                'mike': 'password123',
                'liz': 'pass123'}  # dictionary


def user_input() -> tuple:
    return input('username: '), input('password: ')


def check_user_in_database(user: tuple, database: dict) -> None:
    if (user[0].casefold(), user[1]) in database.items():
        print(f"Welcome to the app, {user[0]}!",
              "We have 3 texts to be analyzed.", sep='\n')
    else:
        print(f'Username or password is invalid. Terminating...')
        quit()


def choice_text() -> int:
    choice = input('Enter an integer btw. 1 and 3 to select: ')
    if choice.isnumeric() and 0 < int(choice) < 4:
        return int(choice)
    print('Invalid input. Terminating...')
    quit()


def handle_statistics_about_text(text: str) -> dict:
    info_text = {'pocet_slov': 0,
                 'pocet_cisel': 0,
                 'soucet_cisel': 0,
                 'pocet_titles': 0,
                 'pocet_slov_uppercase': 0,
                 'pocet_slov_lowercase': 0,
                 'cetnosti_delek_slov': {}}  # evidence pozadovanych statistik o textu
    sep_text = text.split()
    for slovo in sep_text:
        slovo = slovo.strip('.,;')
        info_text['pocet_slov'] += 1
        delka_slova = len(slovo)
        info_text['cetnosti_delek_slov'][delka_slova] = \
            info_text['cetnosti_delek_slov'].setdefault(delka_slova, 0) + 1
        # ve slovniku vytvarim slovnik, ktery eviduje cetnosti jednotlivych delek slov
        if slovo.isnumeric():
            info_text['pocet_cisel'] += 1
            info_text['soucet_cisel'] += int(slovo)
            continue
        if slovo.istitle():
            info_text['pocet_titles'] += 1
            if slovo.isupper():
                info_text['pocet_slov_uppercase'] += 1
        elif slovo.islower():
            info_text['pocet_slov_lowercase'] += 1
    return info_text


def print_statistics(info_text: dict) -> None:
    print(f"There are {info_text['pocet_slov']} words in the selected text.",
          f"There are {info_text['pocet_titles']} titlecase words.",
          f"There are {info_text['pocet_slov_uppercase']} uppercase words.",
          f"There are {info_text['pocet_slov_lowercase']} lowercase words.",
          f"There are {info_text['pocet_cisel']} numeric strings.",
          f"The sum of all the numbers {info_text['soucet_cisel']}.", sep='\n')


def print_occurences(cetnosti: dict) -> None:
    if cetnosti:
        maximalni_cetnost = max(cetnosti.values())
    else:
        maximalni_cetnost = 0
    print(f"LEN | {'OCCURENCES':^{maximalni_cetnost}} | NR.")
    print(ODDELOVAC)
    for znak in sorted(cetnosti):
        hvezdicky = cetnosti[znak] * '*'
        print(f"{znak:>3} | {hvezdicky:<{maximalni_cetnost}} | {cetnosti[znak]:<1}")


print(ODDELOVAC)
uzivatel = user_input()
print(ODDELOVAC)
check_user_in_database(uzivatel, REGISTROVANI)
print(ODDELOVAC)
vyber = choice_text()
statistika = handle_statistics_about_text(TEXTS[vyber - 1])

# Tisk vysledku
print(ODDELOVAC)
print_statistics(statistika)
print(ODDELOVAC)
print_occurences(statistika['cetnosti_delek_slov'])
