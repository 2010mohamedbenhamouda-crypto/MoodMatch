from flask import Flask, jsonify, session
import random, os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "moodmatch-secret-2024")

MOVIES = {
    "happy": [
        {"title": "The Grand Budapest Hotel", "year": 2014, "genre": "Comedy/Adventure", "emoji": "🏨", "desc": "A whimsical tale of a legendary concierge and his protégé."},
        {"title": "Paddington 2", "year": 2017, "genre": "Family/Comedy", "emoji": "🐻", "desc": "The beloved bear navigates London with warmth and charm."},
        {"title": "Singin' in the Rain", "year": 1952, "genre": "Musical", "emoji": "🌧️", "desc": "Hollywood's golden age gets a joyful, song-filled send-up."},
        {"title": "Spirited Away", "year": 2001, "genre": "Animation/Fantasy", "emoji": "🐉", "desc": "A girl's extraordinary journey through a spirit world."},
    ],
    "sad": [
        {"title": "Eternal Sunshine of the Spotless Mind", "year": 2004, "genre": "Drama/Romance", "emoji": "🧠", "desc": "Love, loss, and the memories we can't erase."},
        {"title": "Her", "year": 2013, "genre": "Drama/Sci-Fi", "emoji": "💿", "desc": "A lonely man falls for an AI operating system."},
        {"title": "Manchester by the Sea", "year": 2016, "genre": "Drama", "emoji": "🌊", "desc": "A man must confront his grief and return to his hometown."},
        {"title": "Coco", "year": 2017, "genre": "Animation", "emoji": "🎸", "desc": "A boy's journey to the land of the dead to honor family."},
    ],
    "excited": [
        {"title": "Mad Max: Fury Road", "year": 2015, "genre": "Action/Thriller", "emoji": "🚗", "desc": "A relentless, electrifying chase across a post-apocalyptic wasteland."},
        {"title": "Everything Everywhere All at Once", "year": 2022, "genre": "Sci-Fi/Comedy", "emoji": "🥯", "desc": "A laundromat owner discovers infinite multiverse possibilities."},
        {"title": "Spider-Man: Into the Spider-Verse", "year": 2018, "genre": "Animation/Action", "emoji": "🕷️", "desc": "Miles Morales becomes Spider-Man in a visually stunning adventure."},
        {"title": "Top Gun: Maverick", "year": 2022, "genre": "Action", "emoji": "✈️", "desc": "Maverick pushes limits in an impossible high-stakes mission."},
    ],
    "scared": [
        {"title": "Get Out", "year": 2017, "genre": "Horror/Thriller", "emoji": "👁️", "desc": "A Black man uncovers sinister secrets at his girlfriend's family estate."},
        {"title": "Hereditary", "year": 2018, "genre": "Horror", "emoji": "🏚️", "desc": "A family unravels after a mysterious and terrifying death."},
        {"title": "A Quiet Place", "year": 2018, "genre": "Horror/Sci-Fi", "emoji": "🤫", "desc": "Survival in silence as deadly creatures hunt by sound."},
        {"title": "The Witch", "year": 2015, "genre": "Horror/Period", "emoji": "🐐", "desc": "A Puritan family encounters genuine evil in the New England wilderness."},
    ],
    "bored": [
        {"title": "Knives Out", "year": 2019, "genre": "Mystery/Comedy", "emoji": "🔪", "desc": "A brilliant detective investigates a wealthy patriarch's death."},
        {"title": "The Prestige", "year": 2006, "genre": "Mystery/Drama", "emoji": "🎩", "desc": "Two magicians locked in a dangerous rivalry of obsession."},
        {"title": "Parasite", "year": 2019, "genre": "Thriller/Drama", "emoji": "🏠", "desc": "A poor family schemes their way into a wealthy household."},
        {"title": "Inception", "year": 2010, "genre": "Sci-Fi/Thriller", "emoji": "🌀", "desc": "A thief plants ideas inside targets' dreams within dreams."},
    ],
    "romantic": [
        {"title": "Before Sunrise", "year": 1995, "genre": "Romance/Drama", "emoji": "🌅", "desc": "Two strangers spend one magical night wandering Vienna."},
        {"title": "Call Me By Your Name", "year": 2017, "genre": "Romance/Drama", "emoji": "🍑", "desc": "A summer romance blooms between a teen and a scholar in Italy."},
        {"title": "Portrait of a Lady on Fire", "year": 2019, "genre": "Romance/Drama", "emoji": "🔥", "desc": "A painter and her subject fall in love in 18th century France."},
        {"title": "Amélie", "year": 2001, "genre": "Romance/Comedy", "emoji": "🎠", "desc": "A Parisian woman secretly improves others' lives and finds love."},
    ],
}

MOODS = [
    {"id": "happy",    "label": "Happy",    "emoji": "😄", "color": "#FFD700"},
    {"id": "sad",      "label": "Sad",      "emoji": "😢", "color": "#6B9FD4"},
    {"id": "excited",  "label": "Excited",  "emoji": "🤩", "color": "#FF6B35"},
    {"id": "scared",   "label": "Scared",   "emoji": "😱", "color": "#8B5CF6"},
    {"id": "bored",    "label": "Bored",    "emoji": "😑", "color": "#6EE7B7"},
    {"id": "romantic", "label": "Romantic", "emoji": "🥰", "color": "#F472B6"},
]

# Route 1 — Home: serve the single-page frontend
@app.route("/")
def index():
    with open("index.html") as f:
        return f.read()

# Route 2 — Recommend: random film for a mood + session tracking
@app.route("/recommend/<mood>")
def recommend(mood):
    if mood not in MOVIES:
        return jsonify({"error": "Mood not found"}), 404
    movie = random.choice(MOVIES[mood])
    mood_info = next(m for m in MOODS if m["id"] == mood)
    history = session.get("history", [])
    history.append({"mood": mood, "movie": movie["title"]})
    session["history"] = history[-10:]
    return jsonify({"mood": mood_info, "movie": movie})

# Route 3 — Browse: all films organized by mood
@app.route("/browse")
def browse():
    return jsonify({"moods": MOODS, "movies": MOVIES})

# Route 4 — History: session recommendation log
@app.route("/history")
def history():
    log = session.get("history", [])
    enriched = []
    for item in reversed(log):
        mood_info = next((m for m in MOODS if m["id"] == item["mood"]), None)
        enriched.append({"mood": mood_info, "movie": item["movie"]})
    return jsonify({"history": enriched})

# Route 5 — API: JSON for a specific mood
@app.route("/api/movies/<mood>")
def api_movies(mood):
    if mood not in MOVIES:
        return jsonify({"error": "Mood not found"}), 404
    return jsonify({"mood": mood, "movies": MOVIES[mood]})

if __name__ == "__main__":
    app.run(debug=True)