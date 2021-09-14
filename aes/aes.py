from decrypter import Decrypter
from encryptor import Encryptor
from formatter import Formatter as ftr


def aes():
    """
    Note for grader: You only need to change the strings in lines 10-12.
    cipher_key and input_word can handle byte values to be space-separated if you prefer that.
    """
    cipher_key = ftr.formatted("0f8866b8a9583c8dfb93848e56193d3a117372af1a967846211b87878d5305a7")
    input_word = ftr.formatted("6c8609a5dff9a0e8fdb368b81f41314f")
    action = "ENCRYPT" # must be "ENCRYPT" or"DECRYPT"
    if action == "ENCRYPT":
        print(Encryptor().encrypt(input_word, cipher_key).replace(" ", ""))
    elif action == "DECRYPT":
        print(Decrypter().decrypt(input_word, cipher_key).replace(" ", ""))
    else:
        raise Exception("action must be 'ENCRYPT' or 'DECRYPT' exclusively.")

if __name__ == '__main__':
    aes()

