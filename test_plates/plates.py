def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_digit = ""
    first_index = 0
    tmp = None

    if len(s) > 6 or len(s) < 2:
            return False

    for text in range(len(s)):
        #“No periods, spaces, or punctuation marks are allowed.”
        if s[text] in " .,!?":
            return False

        #Assume that any letters in the user’s input will be uppercase.
        #“All vanity plates must start with at least two letters.”
        elif s[:2].upper().isalpha() == False:
            return False

        # Check digits rule
        for index, character in enumerate(s):
            if character.isdigit():

                # First digit cannot be 0
                if character == "0":
                    return False

                # Once a digit is found, everything after must be digits
                if not s[index:].isdigit():
                    return False

                break  # no need to keep checking after the first digit

    return True

if __name__ == "__main__":
    main()







