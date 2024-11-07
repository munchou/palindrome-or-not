import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def title():
    print(
        """
\t██████╗  █████╗ ██╗     ██╗███╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗███████╗
\t██╔══██╗██╔══██╗██║     ██║████╗  ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔════╝
\t██████╔╝███████║██║     ██║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██╔████╔██║█████╗  
\t██╔═══╝ ██╔══██║██║     ██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══╝  
\t██║     ██║  ██║███████╗██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗
\t╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
"""
    )


def menu():
    clear_screen()
    title()
    list_to_check = []
    ignore_spaces = False
    ignore_punctuation = False
    ignore_digits = False
    cursor_pos = 0
    cursor_end = 3
    cursor_on = ">"
    cursor_off = " "
    choices = ["spaces", "punctuation", "digits"]

    while True:
        proceed = False
        print(
            f"{cursor_on if cursor_pos == 0 else cursor_off} Would you like to ignore {choices[0]}?"
        )
        print(
            f"{cursor_on if cursor_pos == 1 else cursor_off} Would you like to ignore {choices[1]}"
        )
        print(
            f"{cursor_on if cursor_pos == 2 else cursor_off} Would you like to ignore {choices[2]}?"
        )

        while True:
            answer = input(
                f"Ignore (= remove from input) {choices[cursor_pos]} (y/n): "
            ).casefold()
            if answer == "y" or answer == "n":
                break
        if answer == "y" and cursor_pos == 0:
            ignore_spaces = True
        if answer == "y" and cursor_pos == 1:
            ignore_punctuation = True
        if answer == "y" and cursor_pos == 2:
            ignore_digits = True
        cursor_pos += 1
        clear_screen()
        title()

        if cursor_pos == cursor_end:
            print(
                f'Skip spaces: {"Yes" if ignore_spaces else "No"}\nSkip punctuation: {"Yes" if ignore_punctuation else "No"}\nSkip digits: {"Yes" if ignore_digits else "No"}'
            )

            while True:
                proceed = input("\tProceed? (y/n) ").casefold()
                if proceed == "y" or proceed == "n":
                    break
            if proceed == "y":
                break
            cursor_pos = 0
            clear_screen()
            title()

    while True:
        clear_screen()
        title()
        list_to_check.append(
            input("Please enter the word or sentence you wish to check: ")
        )
        while True:
            add_more = input("Add another? (y/n) ").casefold()
            if add_more == "y" or add_more == "n":
                break
            continue
        if add_more == "n":
            break

    return list_to_check, ignore_spaces, ignore_punctuation, ignore_digits


def process_word(word, ignore_spaces, ignore_punctuation, ignore_digits):
    iterations = 0
    if not isinstance(word, str):
        word = str(word)
    word = word.casefold()
    if ignore_spaces:
        word = word.replace(" ", "")
    if not ignore_punctuation and not ignore_digits:
        iterations += 1
        # print(f"Number of iterations for {word}: {iterations}")
        return word, iterations
    length = len(word)
    u = 0
    while length != 0:
        iterations += 1
        if ignore_digits and not ignore_punctuation:
            # removing digits as they are ignored
            if word[u].isdigit() and word[u] != " ":
                char_count = word.count(word[u])
                word = word.replace(word[u], "")
                length -= char_count
                continue
            if length == 1:
                break
            u += 1
            length -= 1
            continue
        if ignore_punctuation and not ignore_digits:
            # removing punctuation as it is ignored
            if not word[u].isalpha() and not word[u].isdigit() and word[u] != " ":
                char_count = word.count(word[u])
                word = word.replace(word[u], "")
                length -= char_count
                continue
            if length == 1:
                break
            u += 1
            length -= 1
            continue

        if ignore_digits and ignore_punctuation:
            # Removing digits and punctuation as they are ignored
            if not word[u].isalpha() and word[u] != " ":
                char_count = word.count(word[u])
                word = word.replace(word[u], "")
                length -= char_count
                continue
            if length == 1:
                break
            u += 1
            length -= 1
            continue

        u += 1
        length -= 1
    # print(f"Number of iterations for {word}: {iterations}")
    return word, iterations


def palindrome_results(words, ignore_spaces, ignore_punctuation, ignore_digits):
    clear_screen()
    title()
    total_iterations = 0
    print(
        f'Settings: {"" if ignore_spaces else "do not "}skip spaces, {"" if ignore_punctuation else "do not "}skip punctuation, {"" if ignore_digits else "do not "}skip digits'
    )
    for word in words:
        word_cf, iterations = process_word(
            word, ignore_spaces, ignore_punctuation, ignore_digits
        )
        print("\n\tProcessed item:", word_cf)
        (
            print(f'"{word}" is a palindrome')
            if word_cf == word_cf[::-1]
            else print(f'"{word}" is not a palindrome')
        )
        total_iterations += iterations
    # print("Total iterations:", total_iterations)


list_examples = [
    "banana",
    "radar",
    "日本語本日",
    "ra1d1ar",
    "ra1da2r",
    "Racecar",
    "race Car",
    "A man, a plan, a canal, Panama!",
]

list_to_check, ignore_spaces, ignore_punctuation, ignore_digits = menu()
palindrome_results(list_to_check, ignore_spaces, ignore_punctuation, ignore_digits)
