def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_left = years_remaining * 52

    return f"you have {weeks_left} weeks left."


print(life_in_weeks(35))
