# program to find leap year or not
def leap_year():
    year=int(input("Enter the year to check (YYYY) : "))
    if year % 100 ==0 and year % 400 == 0 or year % 4 == 0:
        print(f"the year {year} is a leap year")
    else:
        print(f"the year {year} is not a leap year")
leap_year()