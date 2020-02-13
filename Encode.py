
import random


# generates a random letter to be used
# on genkey.
def genrandletter():
    letter = chr(random.randint(31, 126))
    return letter


# generates a key to be used in abcencode
def genkey(instring):
    # Stores which combos have been used to prevent repeated combos
    used_combos = []
    key = ""
    in_used_combos = False

    for c in range(0, 128):
        # Combo creator
        combo = ""
        for i in range(0, 3):
            combo += genrandletter()

        if combo in used_combos:
            in_used_combos = True

        # Repeated combos denier
        while in_used_combos:
            combo = ""
            # Combo creator
            for i in range(0, 3):
                combo += genrandletter()
            if combo not in used_combos:
                in_used_combos = False

        # Attach key combos to used combos
        used_combos.append(combo)

    # Checks if the return should be a string or a list
    if instring is False:
        return used_combos

    elif instring is True:
        for curr_combo in used_combos:
            key += curr_combo
        return key


# Convert the keys to list
def convklist(keyinstr):
    c = 0
    keylist = []
    curkey = ""
    # Counter to check in which part of the key we are
    for d in keyinstr:
        if c != 3:
            curkey += d
            c += 1
        # Adds the key combination to the list
        else:
            keylist.append(curkey)
            curkey = ""
            c = 0
    return keylist


# encodes toencode with ABCcripto
def abcencode(toenconde, shgenkey):
    if shgenkey == True:

        encoded = ""
        key = genkey(False)

        for character in toenconde:

            encoded += (key[ord((str(character)))])

        return encoded, key
    if shgenkey == False


# decodes encoded text
def abcdecode(encoded, key):
    # Stores the information about the current key of encoded
    # to be then located in key.
    curpart = ""
    decoded = ""
    c = 0
    for d in encoded:
        # counter
        if c != 3:
            curpart += d
            c += 1
        else:
            c = 1
            decoded += chr(key.index(curpart))
            curpart = d

    return decoded

encoded,key = abcencode("o liberato e deus")
print(encoded)