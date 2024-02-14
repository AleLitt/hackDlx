
import requests

url = 'https://api.waifu.im/search'
params = {
    'included_tags': ['maid'],
    'height': '>=2000'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    
    # Process the response data as needed
else:
    print('Request failed with status code:', response.status_code)


url = data['images'][0]['url']

filename = "test.jpg"  # You can specify the filename you want to save the image as

from PIL import Image
from art import *
import io

# Now you can use functions and classes from the io module



response = requests.get(url)
if response.status_code == 200:
    image = Image.open(io.BytesIO(response.content))
    image = image.convert('L')  # Convert image to grayscale

    ascii_art = art2text(image)
    print(ascii_art)
else:
    print("Failed to retrieve the image")
