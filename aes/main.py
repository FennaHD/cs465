# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from key_expansion_manager import KeyExpansionManager


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    cipher_key_raw = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"
    cipher_key = cipher_key_raw.replace(" ", "")
    kem = KeyExpansionManager().get_all_words(cipher_key)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')