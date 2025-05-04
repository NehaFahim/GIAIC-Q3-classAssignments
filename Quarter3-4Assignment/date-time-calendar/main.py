import math
import calendar
from datetime import datetime, date, time, timedelta

print("Math Module:\n")

# Value of Pi and e
print("Pi value:", round(math.pi, 4))
print("Euler's number (e):", round(math.e, 4))

# Basic Calculations
print("Square root of 81:", math.sqrt(81))
print("Factorial of 6:", math.factorial(6))
print("3 raised to the power 4:", math.pow(3, 4))

# Logarithms
print("Natural log of 5:", round(math.log(5), 3))
print("Log base 10 of 100:", math.log10(100))

# Trigonometric Example
angle_deg = 30
angle_rad = math.radians(angle_deg)

print(f"\nTrigonometric values for {angle_deg} degrees:")
print("Sine:", round(math.sin(angle_rad), 3))
print("Cosine:", round(math.cos(angle_rad), 3))
print("Tangent:", round(math.tan(angle_rad), 3))

# ----- Date & Time Examples -----
print("\n⏰ DateTime Module:\n")

# Current Date & Time
current = datetime.now()
print("Current date and time:", current)

# Custom Date & Time
custom_date = date(2025, 12, 1)
custom_time = time(9, 15, 0)
print("Custom date:", custom_date)
print("Custom time:", custom_time)

# Formatted Date
formatted = current.strftime("%d-%B-%Y %I:%M %p")
print("Formatted current datetime:", formatted)

# String to DateTime
date_str = "10-04-2025 06:30 PM"
converted = datetime.strptime(date_str, "%d-%m-%Y %I:%M %p")
print("Converted string to datetime:", converted)

# Add/Subtract time
next_week = current + timedelta(days=7)
half_hour_ago = current - timedelta(minutes=30)
print("Date after 7 days:", next_week)
print("Time 30 minutes ago:", half_hour_ago)

# ----- Calendar Module -----
print("\n Calendar Module:\n")

# Show a full calendar of a year
year = 2025
print(f"Calendar of the year {year}:\n")
print(calendar.calendar(year))

# Print a month
print("March 2025 calendar:")
print(calendar.month(2025, 3))

# Leap year check
check_year = 2024
print(f"Is {check_year} a leap year? {calendar.isleap(check_year)}")
