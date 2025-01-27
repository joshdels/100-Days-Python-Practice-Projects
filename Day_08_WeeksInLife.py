def life_in_weeks(age):
  year_left = 90 - int(age)
  weeks_left = year_left*52
  print(f"You've only got {weeks_left}!")


# Call your function with hard coded values
life_in_weeks(89)