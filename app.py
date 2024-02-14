from flask import Flask, jsonify
import requests

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

@app.route('/trump-quote')
def trump_quote():
    quote = get_trump_quote()
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
