"""
Question:

    You are given a date. Your task is to find what the day is on that date.

Input

    A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

    08 05 2015

Output

    Output the correct day in capital letters.

    WEDNESDAY

Hints

    Use weekday function of calender module

"""

import calendar

def main():
    
    month, day, year = map(int, input().split())

    dayId = calendar.weekday(year, month, day)
    print(calendar.day_name[dayId].upper())

if __name__ == "__main__":
    main()