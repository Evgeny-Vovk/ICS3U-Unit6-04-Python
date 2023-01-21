# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: January 2023
# ICS3U-Unit6-04.py File, learning functions with parameters in python.

import random


def table_process(table, amount_of_numbers):
    sum = 0
    for rows in table:
        print("")
        for number in rows:
            sum += number
            average = sum / amount_of_numbers
            print(" {0} ".format(number),end="")
    return average


def main():

    table = []
    counter = 0

    try:
        number_of_rows = int(input("How many rows do you want: "))
        number_of_columns = int(input("How many columns do you want: "))

        amount_of_numbers = number_of_rows * number_of_columns

        while counter < number_of_rows:
            counter2 = 0
            counter += 1
            columns = []
            while counter2 < number_of_columns:
                random_number = random.randint(1, 50)
                columns.append(random_number)
                counter2 += 1
            table.append(columns)

        average = table_process(table, amount_of_numbers)

        print("\nThe average of all numbers is {0:,.2f}.".format(average))
        print("")

    except(ValueError):
        print("Invalid input, please try again.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
