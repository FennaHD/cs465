from decrypter import Decrypter
from encryptor import Encryptor
from formatter import Formatter as ftr


def aes():
    """
    Note for grader: You only need to change the strings in lines 11-13.
    cipher_key and input_word can handle byte values to be space-separated if you prefer that.
    """
    cipher_key = ftr.formatted("000102030405060708090a0b0c0d0e0f1011121314151617")
    input_word = ftr.formatted("00112233445566778899aabbccddeeff")
    action = "ENCRYPT" # must be "ENCRYPT" or"DECRYPT"
    if action == "ENCRYPT":
        Encryptor().encrypt(input_word, cipher_key).replace(" ", "")
    elif action == "DECRYPT":
        Decrypter().decrypt(input_word, cipher_key).replace(" ", "")
    else:
        raise Exception("'action' must be 'ENCRYPT' or 'DECRYPT' exclusively.")

if __name__ == '__main__':
    aes()

