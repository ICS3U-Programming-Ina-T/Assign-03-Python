#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Dec. 11, 2021
# This program determines if a user is
# eligible to vote. It also tests an additional
# person upon the users request


# this function checks if the user is eligible
# to vote
def main():
    # accepts input from user
    user_age_string = input("Enter your age: ")
    print("")

    try:
        user_age_number = int(user_age_string)
        # process & output
        if user_age_number >= 18:
            print("You are eligible to vote!")
            print("")
            age()
        elif user_age_number < 0:
            print("Please enter a valid age.")
        elif user_age_number < 18:
            print("Sorry, you are not eligible to vote.")
            print("You must be 18 or older.")
            print("")
            age()
        else:
            print("Please enter a valid age.")
    except Exception:
        print("{} is not a number. Please enter a valid age.".
              format(user_age_string))


# checks if user wants to test someone else
def age():
    yes = "yes"
    no = "no"
    other_age = (input("Would you like to test someone else? (yes/no): "))

    if other_age == yes:
        print("That's wonderful!")
        print("")
        new()
    elif other_age == no:
        print("")
        print("Thanks for playing!")
    else:
        print("Please enter a valid number.")


# checks the second persons eligibility
def new():
    new_name = (input("Enter their name: "))
    new_age_string = input("Enter their age: ")

    try:
        new_age_int = int(new_age_string)
        print("")

        if new_age_int >= 18:
            print("{} is eligible to vote!". format(new_name))
        elif new_age_int < 0:
            print("Please enter a valid age.")
            new()
        elif new_age_int < 18:
            print("{} is not eligible to vote.". format(new_name))
        else:
            print("Please enter valid data.")
    except Exception:
        print("{} is not a number.". format(new_age_string))


if __name__ == "__main__":
    main()
