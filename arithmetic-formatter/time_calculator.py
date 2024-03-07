def add_time(start, duration, start_day=None):

  # Change format to 24h
  if "PM" in start:
    hour = start.split(":")[0]
    hour = int(hour) + 12
  else:
    hour = start.split(":")[0]
    hour = int(hour)

  start = start.rstrip("AMPM")

  # Add hours
  finish_hour = hour + int(duration.split(":")[0])

  # Add minutes
  minutes = int(duration.split(":")[1]) + int(start.split(":")[1])
  if minutes >= 60:
    hour_count = int(minutes / 60)
    minutes -= hour_count * 60

    # Add full hours from minutes
    finish_hour += hour_count

  # Convert hours to days
  #if finish_hour >= 24:
  day_count = int(finish_hour / 24)
  finish_hour -= day_count * 24

  # Convert to 12h
  ending = 'AM' if finish_hour < 12 else 'PM'
  if finish_hour > 12:
    finish_hour -= 12
  # Format minutes to be 01 ect.
  if minutes < 10:
    minutes = "0" + str(minutes)

  # Days gone
  if start_day != None:
    week = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday'
    ]
    start_day_index = week.index(start_day.capitalize())

    # return index of the finish day in the week

    finish_day_index = (start_day_index + day_count)
    finish_day_index = finish_day_index % 7

  if finish_hour == 0:
    finish_hour = 12

  # Concat
  new_time = f"{str(finish_hour)}:{str(minutes)} {ending}"

  if start_day != None:
    new_time += f", {week[finish_day_index]}"
    if day_count == 1:
      new_time += f" (next day)"
    elif day_count > 1:
      new_time += f" ({day_count} days later)"
  else:
    if day_count == 1:
      new_time += f" (next day)"
    elif day_count > 1:
      new_time += f" ({day_count} days later)"


  return new_time


