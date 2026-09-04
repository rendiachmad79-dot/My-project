import argparse


def greet(name: str, excited: bool = False) -> str:
    suffix = "!" if excited else "."
    return f"Hello, {name}{suffix}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple greeting CLI")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    parser.add_argument("-e", "--excited", action="store_true", help="Add exclamation")
    args = parser.parse_args()
    print(greet(args.name, args.excited))


if __name__ == "__main__":
    main()
