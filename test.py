import requests
# Make a GET request to the API endpoint
response = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/")
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the response
    print(data)
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)