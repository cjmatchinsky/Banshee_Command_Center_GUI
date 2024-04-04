import requests
from datetime import datetime, timedelta
import os
from PyQt5.uic import loadUi

def format_date(input_date):
    date_obj = datetime.strptime(input_date, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%m/%d/%Y")
    return formatted_date

def get_day_of_week(input_date):
    date_obj = datetime.strptime(input_date, "%m/%d/%Y")
    day_of_week = date_obj.strftime("%A")
    return day_of_week

def subtract_one_day(date_str):
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    previous_day = date_obj - timedelta(days=1)
    formatted_date = previous_day.strftime("%m/%d/%Y")
    return formatted_date
 

def image_download(URL_input, number):
  image_url = URL_input
  temp_weather_icon_path = f"weather_icon_images/temp_weatherICON{number}.png"

  # Send a GET request to the URL
  response = requests.get(image_url, stream=True)

  # Check if the request was successful (status code 200)
  if response.status_code == 200:
      # Open a local file with write-binary mode
      with open(temp_weather_icon_path, 'wb') as file:
          # Iterate over the content in chunks and write to the file
          for chunk in response.iter_content(chunk_size=128):
              file.write(chunk)

      #print(f"Image downloaded successfully as {temp_weather_icon_path}")
  else:
      print(f"Failed to download image. Status code: {response.status_code}")

def coordinate_validations(input_coordinate):
    temp = input_coordinate
    # Regular expression to match two floats separated by a comma and a space
    pattern = r'^[-+]?\d+\.\d+, ?[-+]?\d+\.\d+$'
    # Check if the string matches the pattern
    match = re.match(pattern, temp)
    if match:
        print("Valid coordinates string")
        return True
    else:
        print("Invalid coordinates string")
        return False
    
    
def arduino_map(value, from_low, from_high, to_low, to_high):
    """
    Map the value from one range to another.

    Parameters:
    - value: The input value to be mapped.
    - from_low: The lower bound of the input range.
    - from_high: The upper bound of the input range.
    - to_low: The lower bound of the output range.
    - to_high: The upper bound of the output range.

    Returns:
    The mapped value.
    """
    # Ensure the value is within the input range
    value = max(from_low, min(from_high, value))

    # Map the value to the output range
    from_range = from_high - from_low
    to_range = to_high - to_low

    mapped_value = to_low + (value - from_low) * (to_range / from_range)
    return mapped_value