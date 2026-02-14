from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from functools import wraps
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "supersecret"

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["tourism_recommender"]
users_collection = db["users1"]
destinations_collection = db["destinations"]
auth_collection = db["auth_users"]

# -------------------------------
# Decorator to require login
# -------------------------------
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

# -------------------------------
# Signup
# -------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username').strip().lower()
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        name = request.form.get('name')
        email = request.form.get('email')
        contact = request.form.get('contact')
        age = request.form.get('age')
        gender = request.form.get('gender')

        if password != confirm_password:
            return render_template('signup.html', error="Passwords do not match.")

        if auth_collection.find_one({"username": username}):
            return render_template('signup.html', error="Username already exists.")

        auth_collection.insert_one({"username": username, "password": password})
        users_collection.insert_one({
            "username": username,
            "name": name,
            "email": email,
            "contact": contact,
            "age": age,
            "gender": gender
        })

        session['username'] = username
        return redirect(url_for('index'))
    
    return render_template('signup.html')

# -------------------------------
# Login
# -------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip().lower()
        password = request.form.get('password')
        user = auth_collection.find_one({"username": username, "password": password})
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Wrong username or password.")
    return render_template('login.html')

# -------------------------------
# Logout
# -------------------------------
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# -------------------------------
# Main Page (Protected)
# -------------------------------
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        preferences = request.form.getlist('preferences')
        last_destination = request.form.get('last_destination', '')
        review = request.form.get('review', '')
        rating = int(request.form.get('rating', 0))

        user_data = {
            "username": session['username'],
            "preferences": preferences,
            "last_destination": last_destination.strip(),
            "review": review.strip(),
            "rating": rating
        }

        # Save review and rating to destination if destination exists
        if last_destination and review:
            dest_doc = destinations_collection.find_one({"name": last_destination.strip()})
            if dest_doc:
                destinations_collection.update_one(
                    {"_id": dest_doc["_id"]},
                    {"$push": {
                        "reviews": {
                            "username": session['username'],
                            "text": review.strip(),
                            "rating": rating
                        }
                    }}
                )

        users_collection.insert_one(user_data)

        preferences_str = ','.join(preferences) if preferences else ""
        return redirect(url_for('recommendations', preferences=preferences_str))

    return render_template('index.html', error=None)

# -------------------------------
# Recommendations (Protected)
# -------------------------------
@app.route('/recommendations')
def recommendations():
    preferences = request.args.get('preferences', '')
    preference_list = [p.strip() for p in preferences.split(',')] if preferences else []

    # MongoDB query
    if preference_list:
        destinations = list(destinations_collection.find({"attributes": {"$in": preference_list}}, {'_id': 0}))
    else:
        destinations = list(destinations_collection.find({}, {'_id': 0}))

    # Ensure no duplicates
    unique_destinations = []
    seen = set()
    for dest in destinations:
        if "name" in dest and dest["name"] not in seen:
            unique_destinations.append(dest)
            seen.add(dest["name"])

    return render_template(
        'recommendations.html',
        destinations=unique_destinations,
        preferences=preferences  # <<< this is what you're using in HTML
    )

# -------------------------------
# Destination Details (Protected)
# -------------------------------
@app.route('/destination/<destination_name>')
@login_required
def destination_detail(destination_name):
    destination = destinations_collection.find_one({"name": destination_name})
    
    if not destination:
        return "<h2>Destination not found</h2>", 404

    # Load image
    if "image_file" in destination:
        destination["image"] = url_for('static', filename=f"images/{destination['image_file']}")
    else:
        destination["image"] = url_for('static', filename="images/default.jpg")
    
    # Get reviews and calculate average rating
    reviews = destination.get("reviews", [])
    avg_rating = None
    if reviews:
        total = sum(r["rating"] for r in reviews)
        avg_rating = round(total / len(reviews), 1)

    return render_template(
        "destination_detail.html",
        destination=destination,
        reviews=reviews,
        avg_rating=avg_rating
    )

# -------------------------------
# Run the App
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
