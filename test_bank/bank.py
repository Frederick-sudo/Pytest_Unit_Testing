def main():
    try:
        greeting = input("Greeting: ")
    except EOFError:
        return

    print(f"{value(greeting)}")


def value(greeting):
    handed_value = ""

    if "hello" in greeting.strip().lower():
        handed_value = "$0"
        return handed_value

    elif greeting[0].strip().lower() == "h":
        handed_value = "$20"
        return handed_value

    else:
        handed_value = "$100"
        return handed_value


if __name__ == "__main__":
    main()
