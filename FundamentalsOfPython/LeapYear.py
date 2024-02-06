def is_leap_year(year):
    """Determines whether a given year is a leap year."""

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# If you enter 2024 then it print "2024 is a leap year."
