################Task01##############
def mysplit(string):
    list_split = []
    word = ""

    for char in string:
        if char.isspace():
            if word:
                list_split.append(word)
            word = ""
        else:
            word += char

    if word:
        list_split.append(word)

    return list_split

print(mysplit("To be or not to be, that is the question"))

print(mysplit("To be or not to be,that is the question"))

print(mysplit("   "))

print(mysplit(" abc "))

print(mysplit(""))
################Task02##############
number_dict = {'1': ('  #', '  #', '  #', '  #', '  #'),
               '2': ('###', '  #', '###', '#  ', '###'),
               '3': ('###', '  #', '###', '  #', '###'),
               '4': ('# #', '# #', '###', '  #', '  #'),
               '5': ('###', '#  ', '###', '  #', '###'),
               '6': ('###', '#  ', '###', '# #', '###'),
               '7': ('###', '  #', '  #', '  #', '  #'),
               '8': ('###', '# #', '###', '# #', '###'),
               '9': ('###', '# #', '###', '  #', '###'),
               '0': ('###', '# #', '# #', '# #', '###')
               }


def display_number(num):
    if num < 0:
        print("Число має бути невід'ємним.")
        return

    num_str = str(num)

    for level in range(5):
        for digit in num_str:
            print(number_dict[digit][level], end=' ')
        print()


number_input = input('Введіть невід\'ємне ціле число: ')

try:

    number = int(number_input)
    display_number(number)
except ValueError:
    print('Будь ласка, введіть коректне ціле число.')
################Task03##############
text = input("Enter your message: ")
cipher = ''

for char in text:
    if char.isalpha():
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)

print("Encrypted message:", cipher)
################Task04##############
cipher = input('Enter your cryptogram: ')
text = ''

for char in cipher:
    if char.isalpha():
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)

print("Decrypted message:", text)
################Task05##############
def caesar_cipher(text, shift):
    result = ''

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            code = ord(char) + shift

            if is_upper:
                if code > ord('Z'):
                    code -= 26
            else:
                if code > ord('z'):
                    code -= 26

            result += chr(code) if is_upper else chr(code).lower()
        else:
            result += char

    return result


text_to_encrypt = input('Enter the text to encrypt: ')
while True:
    try:
        shift_value = int(input('Enter the shift value (1-25): '))
        if 1 <= shift_value <= 25:
            break
        else:
            print('Please enter a valid shift value in the range of 1 to 25.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')

encrypted_text = caesar_cipher(text_to_encrypt, shift_value)
print('Encrypted text:', encrypted_text)
