from datetime import datetime
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

while(True):
    day1, month1, year1 = input("Please enter the starting day, month and year is this exact order under this format(dd:mm:yyyy):").split(':')
    day1 = int(day1)
    month1 = int(month1)
    year1 = int(year1)
    if day1 > 31 or day1 < 1 or month1 > 12 or month1 < 1 or year1 < 1 or year1 > 9999:
        print("The day must be between 1 and 31\nThe months can be from 1 to 12\nThe year has to be between 1 and 9999")
        continue
    totalDays1 = day1 + month1 * 30 + year1 * 365
    print(f'Your starting date is {months[month1 - 1]} {day1} year {year1}')
    while(True):
        day2, month2, year2 = input("Please enter the ending day, month and year is this exact order, they have to be after the starting date under this format(dd:mm:yyyy):").split(':')
        day2 = int(day2)
        month2 = int(month2)
        year2 = int(year2)
        if day2 > 31 or day2 < 1 or month2 > 12 or month2 < 1 or year2 < 1 or year2 > 9999:
            print("The day must be between 1 and 31\nThe months can be from 1 to 12\nThe year has to be between 1 and 9999")
            continue
        totalDays2 = day2 + month2 * 30 + year2 * 365
        if totalDays1 > totalDays2 or totalDays1 == totalDays2:
            print("The starting date can't be later than the ending date or the same date")
            continue
        break
    break

timeDiff = totalDays2 - totalDays1
if timeDiff / 365 > 0:
    years = timeDiff // 365
    remDays = timeDiff - (365 * years)
    timeDiff -= 365 * years
if timeDiff / 30 > 0:
    months = timeDiff // 30
    remDays = timeDiff - 30 * months
    timeDiff -= months * 30
days = timeDiff

print(f'Time between the give dates is: {years} years, {months} months and {days} days')