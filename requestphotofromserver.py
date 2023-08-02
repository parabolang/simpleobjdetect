import requests
import shutil

# Replace the URL with the actual URL of the image
url = "http://192.168.1.192/cap"

# Send a GET request to the URL
response = requests.get(url, stream=True)

# Save the image to a local file
image_file = "29.jpg"
with open(image_file, "wb") as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

