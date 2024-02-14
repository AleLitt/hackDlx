import requests
from PIL import Image
import io

def fetch_image_and_convert_to_ascii(url):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        image = image.convert('L')  # Convert image to grayscale

        ascii_art = convert_to_ascii(image)
        print(ascii_art)
    else:
        print("Failed to retrieve the image")

def convert_to_ascii(image, width=100):
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width / 2)
    resized_image = image.resize((width, new_height))
    
    ascii_chars = "@%#*+=-:. "
    ascii_str = ""
    for pixel_value in resized_image.getdata():
        ascii_str += ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]
        if len(ascii_str) >= width:
            ascii_str += ""
    return ascii_str
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
# Example usage

fetch_image_and_convert_to_ascii(url)
