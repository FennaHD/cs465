AES

Implementation of the Advanced Encryption Standard (AES). Given a 128-bit hex-string, an arbitrary cipher key of either 128, 192 or 256 bits, and the instruction to encrypt or decrypt as input, the algorithm will return the encrypted/decrypted hex-string.

E.g. `6c8609a5dff9a0e8fdb368b81f41314f` as a 128 bit hex-string would encrypt to `b75b996242ee57218d1b13c10cedad30` using the 256-bit key `0f8866b8a9583c8dfb93848e56193d3a117372af1a967846211b87878d5305a7`.

In order to run, edit `aes/aes.py` by changing the strings in lines 11-13:

`11 cipher_key = ftr.formatted("0f8866b8a9583c8dfb93848e56193d3a117372af1a967846211b87878d5305a7")`  
`12 input_word = ftr.formatted("6c8609a5dff9a0e8fdb368b81f41314f")`  
`13 action = "ENCRYPT" # must be "ENCRYPT" or"DECRYPT"`

Then run by either `python ./aes.py` or `python3 ./aes.py`.

I only looked at the resources listed in the project specification and did not use any additional material.