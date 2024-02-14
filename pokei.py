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
    for y in range(new_height):
        for x in range(width):
            pixel_value = resized_image.getpixel((x, y))
            ascii_str += ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]
        ascii_str += "\n"
    return ascii_str

# Fetch Pokémon data from the PokeAPI
def fetch_pokemon_image(pokemon_name):
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(api_url)
    if response.status_code == 200:
        pokemon_data = response.json()
        sprite_url = pokemon_data['sprites']['front_default']
        return sprite_url
    else:
        print(f"Failed to retrieve data for {pokemon_name}.")
        return None

# Example usage
pokemon_name = input("Enter the name of the Pokemon: ")
image_url = fetch_pokemon_image(pokemon_name)
if image_url:
    print("Pokemon image URL:", image_url)
    fetch_image_and_convert_to_ascii(image_url)
