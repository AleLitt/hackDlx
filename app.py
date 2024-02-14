from flask import Flask, jsonify
import requests
import random

app = Flask(__name__)

def get_trump_quote():
    response = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/")
    if response.status_code == 200:
        data = response.json()
        if data["messages"]:
            return data["messages"]["non_personalized"][0]
        else:
            return "No quotes available."
    else:
        print("Error:", response.status_code)
        return None

def get_kanye_quote():
    response = requests.get("https://api.kanye.rest")
    if response.status_code == 200:
        data = response.json()
        return data.get('quote')
    else:
        print("Failed to retrieve a quote")
        return None

@app.route('/random-quote')
def random_quote():
    if random.choice([True, False]):
        quote = get_trump_quote()
        source = "Trump"
    else:
        quote = get_kanye_quote()
        source = "Kanye"
    return jsonify({"quote": quote, "source": source})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
