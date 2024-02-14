import requests

def get_kanye():
    # The URL of the Kanye Rest API
    url = "https://api.kanye.rest"

    # Sending a GET request to the API
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()
        # Extracting the quote from the response data
        quote = data.get('quote')
        #print(f"Kanye says: \"{quote}\"")
    else:
        print("Failed to retrieve a quote")
    
    return quote

def get_trump():
    # Make a GET request to the API endpoint
    response = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/")
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Print the response
        #print(data)
    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code)
    return data

quote1 = get_kanye()
quote2 = get_trump()

#print(quote1, "\n")
print(quote2)
