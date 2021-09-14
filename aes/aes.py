from decrypter import Decrypter
from encryptor import Encryptor


def print_hi(name):
    cipher_key = formatted("0f8866b8a9583c8dfb93848e56193d3a117372af1a967846211b87878d5305a7")
    input_word = formatted("6c8609a5dff9a0e8fdb368b81f41314f")
    # encrypted = Encryptor().encrypt(input_word, cipher_key)
    print(Decrypter().decrypt(input_word, cipher_key).replace(" ", ""))


def formatted(to_format):
    """
	In order to debug easier while programing the project I only worked with space separated bytes as input.
	Example input doesn't have spaces, so it's easier to handle the key with no spaces in order to just copy
	paste the auto-grader input.
	"""
    return to_format if " " in to_format else " ".join(to_format[i:i + 2] for i in range(0, len(to_format), 2))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

