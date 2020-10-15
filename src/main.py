# Resolve the problem!!
import string
import random
from random import sample

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
CAP_LETTERS = [chr(val) for val in range(65,91)]
LOW_LETTERS = [chr(val) for val in range(97,123)]
DIGITS = list('123456789')
results =[]

def char_sample(list_items,size):
    selected_chars = sample(list_items,size)
    return selected_chars

def generate_password():
    chars=[
        SYMBOLS,
        CAP_LETTERS,
        LOW_LETTERS,
        DIGITS
    ]
    password_size = random.randint(8,16)
    chars_len = len(chars)
    chunk_size = int(password_size / chars_len)
    password =[]

    for i in range(chars_len):
        password.extend(char_sample(chars[i],chunk_size))

    random.shuffle(password)
    return ''.join(password)

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    validity = validate(password)
    results.append(validity)

    #if validate(password):
        #print('Secure Password')
   # else:
        #print('Insecure Password')


if __name__ == '__main__':
    _test_size= 10000
    for i in range(_test_size):
        run()
    count_secure = 0
    count_insecure = 0
    for result in results:
        if(result):
            count_secure += 1
        else:
            count_insecure += 1

    print(f'test size:\t{_test_size}\nSecure passwords:\t{count_secure}\nInsecure passwords:\t{count_insecure}')