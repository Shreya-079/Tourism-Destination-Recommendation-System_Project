# update_best_time.py

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["tourism_recommender"]
collection = db["destinations"]

# destination_data.py

destination_info = {
    "Nainital": {"best_time": "March to June and September to November"},
    "Bhopal": {"best_time": "October to March"},
    "Ellora Caves": {"best_time": "October to March"},
    "Puri": {"best_time": "October to March"},
    "Auli": {"best_time": "December to March"},
    "Ahmedabad": {"best_time": "October to March"},
    "Konark": {"best_time": "October to March"},
    "Munnar": {"best_time": "September to March"},
    "Bhubaneswar": {"best_time": "October to March"},
    "Gulmarg": {"best_time": "December to March"},
    "Jodhpur": {"best_time": "October to March"},
    "Leh": {"best_time": "May to September"},
    "Kodaikanal": {"best_time": "April to June and September to November"},
    "Gokarna": {"best_time": "October to March"},
    "Tirupati": {"best_time": "September to March"},
    "Shillong": {"best_time": "March to June and September to November"},
    "Sundarbans": {"best_time": "September to March"},
    "Bikaner": {"best_time": "October to March"},
    "Haridwar": {"best_time": "October to March"},
    "Tawang": {"best_time": "March to June and September to October"},
    "Alleppey": {"best_time": "November to February"},
    "Pushkar": {"best_time": "October to March"},
    "Dharamshala": {"best_time": "March to June and September to November"},
    "Lucknow": {"best_time": "October to March"},
    "Mahabalipuram": {"best_time": "October to March"},
    "Mussoorie": {"best_time": "March to June and September to November"},
    "Guwahati": {"best_time": "October to April"},
    "Sanchi": {"best_time": "October to March"},
    "Varkala": {"best_time": "October to March"},
    "Pune": {"best_time": "October to February"},
    "Kaziranga": {"best_time": "November to April"},
    "Badami": {"best_time": "October to March"},
    "Cherrapunji": {"best_time": "October to May"},
    "Nagpur": {"best_time": "October to March"},
    "Thanjavur": {"best_time": "October to March"},
    "Lonavala": {"best_time": "June to September and October to March"}
}


# Loop through the dictionary and update each document
for name, data in destination_info.items():
    best_time = data["best_time"]
    result = collection.update_one(
        {"name": name},
        {"$set": {"best_time": best_time}}
    )
    if result.matched_count:
        print(f"✅ Updated best time for: {name}")
    else:
        print(f"❌ Destination not found: {name}")
