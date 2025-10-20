def main():
    try:
        inpt = input("Input: ")
    except EOFError:
        return

    print(f"Output: {shorten(inpt)}")

def shorten(text):
    new_inpt = ''

    for letter in range(len(text)):
        if text[letter].upper() in "AEIOU":
            continue
        else:
            new_inpt += text[letter]

    return new_inpt

if __name__ == "__main__":
    main()







