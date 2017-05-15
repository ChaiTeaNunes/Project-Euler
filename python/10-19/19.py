# Counting Sundays

class IllegalArgumentError(ValueError):
    pass

weekdays = {0:"monday", 1:"tuesday", 2:"wedenesday", 3:"thursday", 4:"friday", 5:"saturday", 6:"sunday",
        "monday":0, "tuesday":1, "wedenesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6 }
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def check_date(month, day, year):
    if month < 1 or month > 12:
        raise IllegalArgumentError("invalid month. argument passed: " + str(month))
    if day < 1 or day > days_in_month[month]:
        raise IllegalArgumentError("invalid day: argument passed: " + str(day))
    if year < 1900:
        raise IllegalArgumentError("invalid year: argument passed: " + str(year))

def is_leap_year(year=1900):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

def days_passed(month=1, day=1, year=1900):
    check_date(month, day, year)
    
    m, y = 1, 1900
    passed = 0
    
    while y != year:
        for i in range(12):
            passed += days_in_month[i+1]
            passed += 1 if i == 2 and is_leap_year(y) else 0
        y += 1
    
    while m != month:
        passed += days_in_month[m]
        passed += 1 if m == 2 and is_leap_year(year) else 0
        m += 1
    
    passed += day - 1
    
    return passed

def day_of_the_week(month=1, day=1, year=1900):
    check_date(month, day, year)
    
    passed = days_passed(month, day, year)
    
    return weekdays[passed % 7]

def count_sundays(start, end):
    smonth, sday, syear = start
    month, day, year = end
    check_date(smonth, sday, syear)
    check_date(month, day, year)
    
    sundays = 0
    
    for y in range(syear, year):
        for m in range(12):
            if day_of_the_week(m+1, 1, y) == "sunday":
                sundays += 1
    
    for m in range(month):
        if day_of_the_week(m+1, 1, year) == "sunday":
            sundays += 1
            
    return sundays
    

start_date = (1, 1, 1901)
end_date = (12, 31, 2000)

print(count_sundays(start_date, end_date))
