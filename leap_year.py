#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is to see if it is a leap year


def main():
    # this function shows formatting output

    # input
    year_as_string = input("Please enter the year: ")
    # process & output
    print("")
    try:
        year_as_int = int(year_as_string)
        if year_as_int % 4 == 0:
            if year_as_int % 100 == 0:
                if year_as_int % 400 == 0:
                    print("It is a leap year")
                else:
                    print("It is not a leap year")
            else:
                print("That is a leap year")
        else:
            print("It is not a leap year")
    except Exception:
        print("That is not an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
