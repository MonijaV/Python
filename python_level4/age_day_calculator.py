from datetime import datetime
def birthday_info(birthdate):
    dob = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    days_lived = (today - dob).days
    day_of_week = dob.strftime("%A")
    return age, days_lived, day_of_week
birthdate = input("Enter birthdate (YYYY-MM-DD): ")
age, days, day = birthday_info(birthdate)
print(f"Age: {age} years")
print(f"Days Lived: {days}")
print(f"Born On: {day}")