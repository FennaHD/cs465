import hashlib as hl
import functools as ft
import os
import binascii

def truncate(digest_bytes):
    # bit size = 8
    # return (int.from_bytes(digest_bytes, "big") >> 152) & 0xff
    # bit size = 12
    # return (int.from_bytes(digest_bytes, "big") >> 148) & 0xfff
    # bit size = 16
    # return (int.from_bytes(digest_bytes, "big") >> 144) & 0xffff
    # bit size = 17
    # return (int.from_bytes(digest_bytes, "big") >> 143) & 0x1ffff
    # bit size = 18
    # return (int.from_bytes(digest_bytes, "big") >> 142) & 0x3ffff
    # bit size = 19
    # return (int.from_bytes(digest_bytes, "big") >> 141) & 0x7ffff
    # bit size = 20
    # return (int.from_bytes(digest_bytes, "big") >> 140) & 0xfffff
    # bit size = 23
    # return (int.from_bytes(digest_bytes, "big") >> 137) & 0x7fffff
    # bit size = 26
    # return (int.from_bytes(digest_bytes, "big") >> 134) & 0x2ffffff
    # bit size = 29
    # return (int.from_bytes(digest_bytes, "big") >> 131) & 0x5ffffff
    # bit size = 32
    return (int.from_bytes(digest_bytes, "big") >> 128) & 0xffffffff

def random_hex_byte():
    return binascii.b2a_hex(os.urandom(20))

def collision():
    h = hl.sha1(random_hex_byte())

    hex_digest = h.hexdigest()
    truncated_digest = truncate(h.digest())

    print(hex_digest)
    print(truncated_digest)

    matches = []
    num_attempts = 0

    hash_dict = {}
    for i in range(50):
        while True:
            num_attempts = num_attempts + 1
            if num_attempts % 100 == 0:
                print(num_attempts)
            new_sample = random_hex_byte()
            new_hash = hl.sha1(new_sample)
            new_hash_digest = new_hash.digest()
            truncated_new_digest = truncate(new_hash_digest)
            if truncated_new_digest in hash_dict:
                matches.append(num_attempts)
                num_attempts = 0
                hash_dict = {}
                break
            else:
                hash_dict[truncated_new_digest] = True

    average = int(ft.reduce(lambda a, b: a + b, matches))/len(matches)
    print(average)

def preimage():
    h = hl.sha1(random_hex_byte())

    hex_digest = h.hexdigest()
    truncated_digest = truncate(h.digest())

    print(hex_digest)
    print(truncated_digest)

    matches = []
    num_attempts = 0

    for i in range(50):
        while True:
            num_attempts = num_attempts + 1
            if num_attempts % 100 == 0:
                print(num_attempts)
            new_sample = random_hex_byte()
            new_hash_digest = hl.sha1(new_sample).digest()
            if truncate(new_hash_digest) == truncated_digest:
                matches.append(num_attempts)
                num_attempts = 0
                break

    average = int(ft.reduce(lambda a, b: a + b, matches))/len(matches)
    print(average)

if __name__ == '__main__':
    """
    In order to run, change line below to either collision() or preimage().
    In order to change bitsize uncomment to appropriate line in truncate()
    """
    collision()

