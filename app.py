from flask import Flask, jsonify
import random, re, feedparser
from datetime import datetime

app = Flask(__name__)

KEYWORDS = {
    "trump": 10, "biden": 10, "ai": 9, "crypto": 9, "elon": 8,
    "vaccine": 8, "aliens": 9, "baby": 6, "stimulus": 6,
    "truth": 7, "bomb": 7, "war": 8, "ceo": 7, "nuke": 10,
    "collapse": 9, "chatgpt": 8, "china": 7, "lizard": 10,
    "putin": 9, "ww3": 10, "matrix": 6, "ghost": 5
}

RSS_FEEDS = [
    "https://rss.cnn.com/rss/cnn_topstories.rss",
    "https://feeds.foxnews.com/foxnews/latest",
    "https://www.nbcnews.com/id/3032091/device/rss/rss.xml",
    "https://www.cbsnews.com/latest/rss/main",
]

def fetch_memes(count=10):
    entries = []
    for url in RSS_FEEDS:
        d = feedparser.parse(url)
        entries.extend(d.entries)

    memes = []
    for entry in entries:
        title = re.sub(r"[^\w\s]", "", entry.title.lower())
        score = sum([KEYWORDS.get(word, 0) for word in title.split()])
        if score > 0:
            name = "Lil" + random.choice(title.split()).capitalize() + "Coin"
            memes.append({"name": name, "score": score})
    memes = sorted(memes, key=lambda x: x["score"], reverse=True)
    return memes[:count]

@app.route("/")
def home():
    return "🧠 RP3K backend is live."

@app.route("/memes")
def memes():
    return jsonify(fetch_memes())
