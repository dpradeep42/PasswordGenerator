import array
import random
import string


def generate(MAX_LEN):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = list(string.ascii_lowercase)
    UPCASE_CHARACTERS = list(string.ascii_uppercase)
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = str(random.randint(0, 9))
    rand_upper = random.choice(string.ascii_uppercase)
    rand_lower = random.choice(string.ascii_lowercase)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    print(password)


if __name__ == '__main__':
    generate(int(input("Enter the Length of the Requred Password: ")))

