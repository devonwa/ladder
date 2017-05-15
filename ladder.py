"""Define functionality for interaction from the command line."""

import argparse


def main():
    parser = argparse.ArgumentParser(desciption='Executes ladder logic.')
    parser.add_argument('proj', metavar='PROJECT_FILE', nargs=1)
    args = parser.parse_args()
    

if __name__ == "__main__":
    main()
