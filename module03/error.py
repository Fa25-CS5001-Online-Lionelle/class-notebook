MY_CONSTANT: int = 42


def takes_string(x: str) -> None:
    print(x.upper())


def main() -> None:
    takes_string("Aloha")


if __name__ == "__main__":
    main()
