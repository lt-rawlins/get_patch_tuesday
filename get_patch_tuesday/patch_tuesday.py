#!/usr/bin/env python3
import calendar
import datetime
import argparse

def main():
    # get the current year
    now = datetime.datetime.now().year

    parser = argparse.ArgumentParser(
        description="Get patch tuesday for a given year. Current year by default."
    )
    parser.add_argument(
        "year", nargs="?", help="The year, example 2020", default=now, type=int
    )
    args = parser.parse_args()

    for month in range(1, 13):
        cal = calendar.monthcalendar(args.year, month)
        # Second Tuesday will be in the second or third week of the month
        week2 = cal[1]
        week3 = cal[2]

        # Check if Tuesday is between 8 and 14. If so Second tuesday is in week 2. Else it's week 3
        if 8 <= week2[calendar.TUESDAY] <= 14:
            patchday = week2[calendar.TUESDAY]
        else:
            patchday = week3[calendar.TUESDAY]
        print(calendar.month_name[month], patchday, args.year)
    # get the current year
    now = datetime.datetime.now().year

    parser = argparse.ArgumentParser(
        description="Get patch tuesday for a given year. Current year by default."
    )
    parser.add_argument(
        "year", nargs="?", help="The year, example 2020", default=now, type=int
    )
    args = parser.parse_args()

    for month in range(1, 13):
        cal = calendar.monthcalendar(args.year, month)
        # Second Tuesday will be in the second or third week of the month
        week2 = cal[1]
        week3 = cal[2]

        # Check if Tuesday is between 8 and 14. If so Second tuesday is in week 2. Else it's week 3
        if 8 <= week2[calendar.TUESDAY] <= 14:
            patchday = week2[calendar.TUESDAY]
        else:
            patchday = week3[calendar.TUESDAY]
        print(calendar.month_name[month], patchday, args.year)

if __name__ == "__main__":
    main()