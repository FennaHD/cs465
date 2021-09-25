from sha1 import sha1

if __name__ == '__main__':
    """
    Given a message and an already computed MAC with an unknown key, performs an extension attack.
    Note that all values are hardcoded to work only with the given values.
    Essentially, we take the old message and calculate the blocks that the hash algorithm would
    have return. i.e. old_message + padding+ 64 bit length. The sha1.py script is slightly modified
    (lines 73-39, 86-89) so that the initializer vector is actually the given MAC in oder to trick
    it into thinking that we are "continuing" the hash algorithm.
    """
    old_message = "4e6f206f6e652068617320636f6d706c65746564206c6162203220736f20676976652" \
                  "07468656d20616c6c20612030"  # "No one has completed lab 2 so give them all a 0"
    old_padding = "80" + (56 * "00")  # 10000...
    old_length = "00000000000001f8"  # 16 bytes (key) + 47 bytes (message) = 63 bytes = 504 bits

    extension = "2e2050533a20486f6e65792c207768657265206973206d792" \
                "0737570657220737569743f" # ". PS: Honey, where is my super suit?"
    print(f'New MAC: {sha1(bytearray.fromhex(extension))}')

    new_message = old_message + old_padding + old_length + extension
    print(f'New message: {new_message}')