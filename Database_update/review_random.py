import random
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["tourism_recommender"]
destinations = db["destinations"]

# Sample review pool
sample_reviews = [
    {"username": "urban_escapist", "text": "A perfect weekend getaway. Peaceful and rejuvenating.", "rating": 5},
    {"username": "chai_and_trails", "text": "Loved the local food and friendly people!", "rating": 4},
    {"username": "history_buff07", "text": "Fascinating heritage site with great guides.", "rating": 5},
    {"username": "beachy_breezy", "text": "Sand was hot, but the view was worth it!", "rating": 4},
    {"username": "rainy_roads", "text": "Weather was unpredictable, but added charm to the experience.", "rating": 4},
    {"username": "snapshots_sam", "text": "Captured some of my best photos here!", "rating": 5},
    {"username": "yoga_travels", "text": "So calm and scenic, ideal for meditation and walks.", "rating": 5},
    {"username": "midnight_roamer", "text": "The night view was magical!", "rating": 5},
    {"username": "foodnfootprints", "text": "Not many options for vegetarians, but the scenery was top notch.", "rating": 3},
    {"username": "hiking_hearts", "text": "Hiking trail was harder than expected but rewarding.", "rating": 4},
    {"username": "solo_travel_soul", "text": "Met some lovely fellow travelers. Felt safe and inspired!", "rating": 5},
    {"username": "roadtrip_rebel", "text": "The journey there was more scenic than the destination.", "rating": 3},
    {"username": "map_marker", "text": "A hidden gem! Not too touristy, just how I like it.", "rating": 5},
    {"username": "sunset_stalker", "text": "Caught the best sunset of my life here!", "rating": 5},
    {"username": "lazy_traveler", "text": "Too much walking involved. Not my cup of tea.", "rating": 2}
]


# Loop through all destinations and assign random reviews
for destination in destinations.find():
    review_count = random.randint(2, 5)  # Number of reviews to assign
    random_reviews = random.sample(sample_reviews, k=review_count)
    destinations.update_one(
        {"_id": destination["_id"]},
        {"$set": {"reviews": random_reviews}}
    )

print("✅ Random reviews added to all destinations.")
