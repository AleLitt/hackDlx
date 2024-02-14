const express = require('express');
const fetch = require('node-fetch');
const app = express();
const PORT = 5000;

async function getTrumpQuote() {
    try {
        const response = await fetch("https://api.whatdoestrumpthink.com/api/v1/quotes/");
        if (response.ok) {
            const data = await response.json();
            return data.messages && data.messages.non_personalized ? data.messages.non_personalized[0] : "No quotes available.";
        } else {
            console.log("Error:", response.status);
            return null;
        }
    } catch (error) {
        console.error("Failed to retrieve Trump quote:", error);
        return null;
    }
}

async function getKanyeQuote() {
    try {
        const response = await fetch("https://api.kanye.rest");
        if (response.ok) {
            const data = await response.json();
            return data.quote;
        } else {
            console.log("Failed to retrieve Kanye quote");
            return null;
        }
    } catch (error) {
        console.error("Failed to retrieve Kanye quote:", error);
        return null;
    }
}

app.get('/random-quote', async (req, res) => {
    const quoteSource = Math.random() < 0.5 ? "Trump" : "Kanye";
    let quote;
    if (quoteSource === "Trump") {
        quote = await getTrumpQuote();
    } else {
        quote = await getKanyeQuote();
    }
    res.json({"quote": quote, "source": quoteSource});
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
