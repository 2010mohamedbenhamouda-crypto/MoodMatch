🎬 MoodMatch — Find Your Film

Tell us how you feel. We'll find the perfect film.

MoodMatch is a Flask web app that recommends movies based on your current mood. Pick from 6 moods, get a handpicked recommendation, and explore a curated library of films — all in a sleek, dark-themed interface.

🚀 Quick Start
bash# 1. Clone the repo
git clone https://github.com/yourusername/moodmatch.git
cd moodmatch

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
Open http://localhost:5000 in your browser.

📋 Routes
RouteMethodDescription/GETHome page — pick a mood/recommend/<mood>GETGet a random film for a mood/browseGETBrowse all films by mood/historyGETView your recommendation history (session-based)/api/movies/<mood>GETJSON API — returns films for a mood
Valid moods: happy, sad, excited, scared, bored, romantic

🗂️ Project Structure
moodmatch/
├── app.py                 # Flask application + routes
├── requirements.txt       # Python dependencies
├── README.md
└── templates/
    ├── base.html          # Shared layout, navigation, styles
    ├── index.html         # Home / mood picker
    ├── recommend.html     # Movie recommendation page
    ├── browse.html        # Full film library
    └── history.html       # Session recommendation history

🎨 Features

6 mood categories with 4 handpicked films each (24 total)
Random recommendation engine — hit "different pick" for variety
Session history — tracks your recommendations this visit
JSON API at /api/movies/<mood> for programmatic access
Responsive dark-themed UI with smooth animations
No database required — all data lives in app.py


🌐 Deployment (Render)

Push to GitHub
Create a new Web Service on render.com
Connect your repo, set:

Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app


Add gunicorn to requirements.txt
Deploy!


🔧 Tech Stack

Backend: Python 3 + Flask
Frontend: Jinja2 templates, vanilla CSS, no frameworks
Fonts: Playfair Display + DM Sans (Google Fonts)
Session storage: Flask's built-in client-side sessions


📝 CRF Requirements Met
RequirementHow it's metFlask backendapp.py — Flask app with routes, templates, sessions3+ routes5 routes: /, /recommend/<mood>, /browse, /history, /api/movies/<mood>Unique & functionalMood-based film recommender with session tracking + JSON APIStyled while codingCSS-in-templates with custom properties, animations, responsive gridREADMEYou're reading it!

💡 Extending the Project

Add a database (SQLite + SQLAlchemy) to persist history across sessions
Add user accounts with Flask-Login
Integrate a real movie API (TMDb) for posters and ratings
Add a "dislike" system that avoids previously shown films
