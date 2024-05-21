#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (num & 1 << 7 and not (num & 1 << 6)):
                return False

        num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [
        80,
        121,
        116,
        104,
        111,
        110,
        32,
        105,
        115,
        32,
        99,
        111,
        111,
        108,
        33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
