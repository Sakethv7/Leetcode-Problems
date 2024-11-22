class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap_year(year: int) -> bool:
            """Check if a year is a leap year."""
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
      
        def days_in_month(year: int, month: int) -> int:
            """Calculate the number of days in a month for a given year."""
            # Days in each month. For February in a leap year, add an extra day.
            days_per_month = [
                31,
                28 + int(is_leap_year(year)),
                31,
                30,
                31,
                30,
                31,
                31,
                30,
                31,
                30,
                31,
            ]
            # Return the number of days in the specified month.
            return days_per_month[month - 1]

        def calculate_days(date: str) -> int:
            """Calculate the total number of days from a fixed date to the given date."""
            # Extract year, month, and day as integers from the date string.
            year, month, day = map(int, date.split("-"))
          
            # Initialize the days counter.
            days = 0
          
            # Count days for the full years up to the given year.
            for y in range(1971, year):
                days += 365 + int(is_leap_year(y))
          
            # Count days for the full months in the given year.
            for m in range(1, month):
                days += days_in_month(year, m)
          
            # Add the days in the given month.
            days += day
            return days

        # Calculate the total days for each date and return their absolute difference.
        return abs(calculate_days(date1) - calculate_days(date2))