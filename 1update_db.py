from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["tourism_recommender"]
collection = db["destinations"]

# Updates for all 100 destinations
updates = {
    "Maldives": {
        "description": "A tropical paradise with overwater bungalows and turquoise lagoons.",
        "fun_facts": [
            "Made up of 26 atolls and over 1,000 islands.",
            "Known for its glowing bioluminescent beaches."
        ],
        "places_to_visit": ["Male", "Hulhumale Beach", "Vaadhoo Island", "Baa Atoll"],
        "best_time": "November to April"
    },
    "Goa": {
        "description": "A vibrant beach paradise known for its nightlife, culture, and Portuguese architecture.",
        "fun_facts": [
            "Was a Portuguese colony until 1961.",
            "Famous for its New Year and Sunburn Festival."
        ],
        "places_to_visit": ["Baga Beach", "Fort Aguada", "Dudhsagar Falls", "Basilica of Bom Jesus"],
        "best_time": "November to February"
    },
    "Swiss Alps": {
        "description": "A majestic mountain range offering world-class skiing and breathtaking views.",
        "fun_facts": [
            "Home to the Matterhorn, one of the most famous peaks.",
            "Hosts the highest railway station in Europe."
        ],
        "places_to_visit": ["Zermatt", "Jungfraujoch", "Interlaken", "Lauterbrunnen"],
        "best_time": "December to March"
    },
    "Himalayas": {
        "description": "The world’s highest mountain range, steeped in spirituality and natural beauty.",
        "fun_facts": [
            "Contains 9 of the 10 highest peaks on Earth.",
            "A sacred region for multiple religions."
        ],
        "places_to_visit": ["Everest Base Camp", "Kedarnath", "Gangotri", "Manali"],
        "best_time": "April to June"
    },
    "Paris": {
        "description": "The romantic capital of France, famed for art, culture, and cuisine.",
        "fun_facts": [
            "The Eiffel Tower was meant to be temporary.",
            "Home to the world’s largest art museum, the Louvre."
        ],
        "places_to_visit": ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Montmartre"],
        "best_time": "April to June and September to October"
    },
    "Tokyo": {
        "description": "A futuristic metropolis blending ancient temples with neon-lit streets.",
        "fun_facts": [
            "Has more Michelin-starred restaurants than any other city.",
            "Hosts the world’s busiest pedestrian crossing."
        ],
        "places_to_visit": ["Shibuya Crossing", "Tokyo Tower", "Asakusa", "Shinjuku"],
        "best_time": "March to May and September to November"
    },
    "Machu Picchu": {
        "description": "An ancient Incan city perched high in the Andes Mountains.",
        "fun_facts": [
            "Rediscovered in 1911 by Hiram Bingham.",
            "A UNESCO World Heritage Site."
        ],
        "places_to_visit": ["Machu Picchu Citadel", "Huayna Picchu", "Sun Gate", "Aguas Calientes"],
        "best_time": "May to September"
    },
    "Rome": {
        "description": "The Eternal City, rich with ancient ruins and Renaissance art.",
        "fun_facts": [
            "Founded in 753 BC according to legend.",
            "The Colosseum could hold 50,000 spectators."
        ],
        "places_to_visit": ["Colosseum", "Roman Forum", "Pantheon", "Vatican City"],
        "best_time": "April to June and September to October"
    },
    "Santorini": {
        "description": "A stunning Greek island with whitewashed villages and volcanic beaches.",
        "fun_facts": [
            "Formed by a massive volcanic eruption.",
            "Famous for its dramatic sunsets."
        ],
        "places_to_visit": ["Oia", "Fira", "Red Beach", "Akrotiri"],
        "best_time": "April to June and September to October"
    },
    "New York City": {
        "description": "The bustling Big Apple, known for skyscrapers and cultural diversity.",
        "fun_facts": [
            "The Statue of Liberty was a gift from France.",
            "Times Square sees 50 million visitors annually."
        ],
        "places_to_visit": ["Statue of Liberty", "Times Square", "Central Park", "Empire State Building"],
        "best_time": "April to June and September to November"
    },
    "Bali": {
        "description": "A tropical haven with lush rice fields, beaches, and Hindu temples.",
        "fun_facts": [
            "Known as the 'Island of the Gods.'",
            "Has over 10,000 temples."
        ],
        "places_to_visit": ["Uluwatu Temple", "Ubud Monkey Forest", "Tanah Lot", "Seminyak Beach"],
        "best_time": "May to September"
    },
    "Banff": {
        "description": "A scenic mountain town in Canada’s Rockies with turquoise lakes.",
        "fun_facts": [
            "Canada’s first national park.",
            "Lake Louise turns bright turquoise in summer."
        ],
        "places_to_visit": ["Lake Louise", "Banff Gondola", "Moraine Lake", "Johnston Canyon"],
        "best_time": "June to August and December to March"
    },
    "London": {
        "description": "A historic city blending royal heritage with modern vibrancy.",
        "fun_facts": [
            "Big Ben is actually the clock tower’s nickname.",
            "The Tube is the world’s oldest underground railway."
        ],
        "places_to_visit": ["Big Ben", "Tower Bridge", "British Museum", "Buckingham Palace"],
        "best_time": "March to May and September to November"
    },
    "Cairo": {
        "description": "A bustling city on the Nile, home to ancient pyramids and bazaars.",
        "fun_facts": [
            "The Great Pyramid is the only remaining Seven Wonders.",
            "Cairo is called 'the city of a thousand minarets.'"
        ],
        "places_to_visit": ["Giza Pyramids", "Sphinx", "Egyptian Museum", "Khan el-Khalili"],
        "best_time": "October to April"
    },
    "Phuket": {
        "description": "Thailand’s largest island, famed for beaches and vibrant nightlife.",
        "fun_facts": [
            "Known for its Big Buddha statue.",
            "A major filming location for James Bond."
        ],
        "places_to_visit": ["Patong Beach", "Big Buddha", "Phi Phi Islands", "Old Phuket Town"],
        "best_time": "November to April"
    },
    "Mount Kilimanjaro": {
        "description": "Africa’s tallest peak, offering a challenging climb and stunning views.",
        "fun_facts": [
            "A dormant volcano with three cones.",
            "The summit is called Uhuru Peak."
        ],
        "places_to_visit": ["Kilimanjaro National Park", "Marangu Gate", "Machame Route", "Shira Plateau"],
        "best_time": "January to March and June to October"
    },
    "Sydney": {
        "description": "A coastal city with iconic landmarks and beautiful beaches.",
        "fun_facts": [
            "The Sydney Opera House has over 1 million tiles.",
            "Hosts one of the world’s largest New Year’s fireworks."
        ],
        "places_to_visit": ["Sydney Opera House", "Harbour Bridge", "Bondi Beach", "Royal Botanic Garden"],
        "best_time": "September to November and March to May"
    },
    "Athens": {
        "description": "The cradle of Western civilization, rich with ancient history.",
        "fun_facts": [
            "Birthplace of the Olympic Games.",
            "The Parthenon was built in 447 BC."
        ],
        "places_to_visit": ["Acropolis", "Parthenon", "Plaka", "National Archaeological Museum"],
        "best_time": "April to June and September to October"
    },
    "Hawaii": {
        "description": "A volcanic archipelago with lush landscapes and pristine beaches.",
        "fun_facts": [
            "Home to the world’s most active volcano, Kilauea.",
            "The only U.S. state with a royal palace."
        ],
        "places_to_visit": ["Waikiki Beach", "Hawaii Volcanoes National Park", "Hanauma Bay", "Pearl Harbor"],
        "best_time": "April to June and September to November"
    },
    "Andes": {
        "description": "A vast mountain range spanning seven countries with rich history.",
        "fun_facts": [
            "The longest mountain range in the world.",
            "Home to the highest capital city, La Paz."
        ],
        "places_to_visit": ["Machu Picchu", "Cusco", "Sacred Valley", "Lake Titicaca"],
        "best_time": "May to September"
    },
    "Barcelona": {
        "description": "A vibrant city with Gaudí architecture, beaches, and lively culture.",
        "fun_facts": [
            "La Sagrada Familia has been under construction since 1882.",
            "Hosts the world’s largest football stadium."
        ],
        "places_to_visit": ["Sagrada Familia", "Park Güell", "La Rambla", "Barceloneta Beach"],
        "best_time": "April to June and September to October"
    },
    "Petra": {
        "description": "A rock-carved city in the desert, once a thriving trade hub.",
        "fun_facts": [
            "Known as the 'Rose City' due to its stone color.",
            "Featured in Indiana Jones and the Last Crusade."
        ],
        "places_to_visit": ["The Treasury", "Siq Canyon", "Royal Tombs", "Monastery"],
        "best_time": "March to May and September to November"
    },
    "Miami": {
        "description": "A sunny coastal city with vibrant nightlife and Art Deco charm.",
        "fun_facts": [
            "Has the largest collection of Art Deco buildings.",
            "A gateway to the Everglades."
        ],
        "places_to_visit": ["South Beach", "Wynwood Walls", "Everglades National Park", "Ocean Drive"],
        "best_time": "November to April"
    },
    "Rocky Mountains": {
        "description": "A rugged range in North America, perfect for outdoor adventures.",
        "fun_facts": [
            "Spans five U.S. states and two Canadian provinces.",
            "Home to the Continental Divide."
        ],
        "places_to_visit": ["Rocky Mountain National Park", "Aspen", "Banff", "Yellowstone"],
        "best_time": "June to September"
    },
    "Istanbul": {
        "description": "A city straddling two continents, rich in history and culture.",
        "fun_facts": [
            "Once known as Constantinople.",
            "The Hagia Sophia has been both a church and a mosque."
        ],
        "places_to_visit": ["Hagia Sophia", "Blue Mosque", "Topkapi Palace", "Grand Bazaar"],
        "best_time": "March to May and September to November"
    },
    "Dubai": {
        "description": "A futuristic desert city with towering skyscrapers and luxury.",
        "fun_facts": [
            "Home to the world’s tallest building, Burj Khalifa.",
            "Has man-made islands shaped like a palm tree."
        ],
        "places_to_visit": ["Burj Khalifa", "Dubai Mall", "Palm Jumeirah", "Desert Safari"],
        "best_time": "November to March"
    },
    "Bora Bora": {
        "description": "A luxurious Polynesian island with stunning lagoons and overwater villas.",
        "fun_facts": [
            "A volcanic island surrounded by a coral reef.",
            "Known as a top honeymoon destination."
        ],
        "places_to_visit": ["Matira Beach", "Mount Otemanu", "Coral Gardens", "Lagoonarium"],
        "best_time": "May to October"
    },
    "Yosemite": {
        "description": "A natural wonder with towering cliffs, waterfalls, and giant sequoias.",
        "fun_facts": [
            "El Capitan is a mecca for rock climbers.",
            "Home to the world’s largest single granite rock."
        ],
        "places_to_visit": ["Yosemite Valley", "El Capitan", "Half Dome", "Bridalveil Fall"],
        "best_time": "May to September"
    },
    "Kyoto": {
        "description": "A historic city of temples, gardens, and traditional Japanese culture.",
        "fun_facts": [
            "Was Japan’s capital for over 1,000 years.",
            "Famous for its geisha districts."
        ],
        "places_to_visit": ["Fushimi Inari Shrine", "Kinkaku-ji", "Arashiyama Bamboo Grove", "Gion"],
        "best_time": "March to May and October to November"
    },
    "Cape Town": {
        "description": "A coastal gem with dramatic mountains and vibrant culture.",
        "fun_facts": [
            "Table Mountain is one of the New Seven Wonders of Nature.",
            "The southernmost tip of Africa is nearby."
        ],
        "places_to_visit": ["Table Mountain", "Cape Point", "Robben Island", "V&A Waterfront"],
        "best_time": "December to March"
    },
    "Venice": {
        "description": "A romantic city of canals, bridges, and Renaissance architecture.",
        "fun_facts": [
            "Built on 118 small islands.",
            "Has no roads, only canals and walkways."
        ],
        "places_to_visit": ["St. Mark’s Basilica", "Grand Canal", "Rialto Bridge", "Doge’s Palace"],
        "best_time": "April to June and September to October"
    },
    "Great Barrier Reef": {
        "description": "The world’s largest coral reef system, teeming with marine life.",
        "fun_facts": [
            "Visible from space.",
            "Home to over 1,500 species of fish."
        ],
        "places_to_visit": ["Cairns", "Green Island", "Agincourt Reef", "Heart Reef"],
        "best_time": "June to November"
    },
    "Mount Everest": {
        "description": "The highest peak on Earth, a bucket-list climb for adventurers.",
        "fun_facts": [
            "Stands at 8,848 meters (29,029 feet).",
            "First summited by Edmund Hillary and Tenzing Norgay in 1953."
        ],
        "places_to_visit": ["Everest Base Camp", "Namche Bazaar", "Tengboche Monastery", "Lukla"],
        "best_time": "April to May and September to October"
    },
    "Jerusalem": {
        "description": "A sacred city with deep religious and historical significance.",
        "fun_facts": [
            "Holy to Judaism, Christianity, and Islam.",
            "The Old City is a UNESCO World Heritage Site."
        ],
        "places_to_visit": ["Western Wall", "Church of the Holy Sepulchre", "Dome of the Rock", "Mount of Olives"],
        "best_time": "March to May and September to November"
    },
    "Rio de Janeiro": {
        "description": "A lively coastal city famous for Carnival and stunning beaches.",
        "fun_facts": [
            "Christ the Redeemer is one of the New Seven Wonders.",
            "Hosts the world’s largest Carnival celebration."
        ],
        "places_to_visit": ["Christ the Redeemer", "Copacabana Beach", "Sugarloaf Mountain", "Ipanema Beach"],
        "best_time": "December to March"
    },
    "Prague": {
        "description": "A fairy-tale city with cobblestone streets and Gothic architecture.",
        "fun_facts": [
            "Known as the 'City of a Hundred Spires.'",
            "The Prague Castle is the largest ancient castle in the world."
        ],
        "places_to_visit": ["Prague Castle", "Charles Bridge", "Old Town Square", "Astronomical Clock"],
        "best_time": "April to June and September to October"
    },
    "Seychelles": {
        "description": "An idyllic island nation with pristine beaches and unique granite boulders.",
        "fun_facts": [
            "Home to the rare coco de mer nut.",
            "A haven for endangered species like the giant tortoise."
        ],
        "places_to_visit": ["Anse Lazio", "Vallee de Mai", "Mahe Island", "La Digue"],
        "best_time": "April to May and October to November"
    },
    "Pyrenees": {
        "description": "A scenic mountain range between Spain and France, ideal for hiking.",
        "fun_facts": [
            "Forms a natural border between two countries.",
            "Home to the tiny nation of Andorra."
        ],
        "places_to_visit": ["Ordesa National Park", "Gavarnie Cirque", "Andorra la Vella", "Pic du Midi"],
        "best_time": "June to September"
    },
    "Shanghai": {
        "description": "A modern metropolis with a blend of skyscrapers and historic charm.",
        "fun_facts": [
            "The Bund showcases colonial-era buildings.",
            "Has the world’s fastest commercial train."
        ],
        "places_to_visit": ["The Bund", "Shanghai Tower", "Yu Garden", "Nanjing Road"],
        "best_time": "March to May and September to November"
    },
    "Angkor Wat": {
        "description": "A massive temple complex, the largest religious monument in the world.",
        "fun_facts": [
            "Built in the 12th century by the Khmer Empire.",
            "Featured on Cambodia’s national flag."
        ],
        "places_to_visit": ["Angkor Wat", "Bayon Temple", "Ta Prohm", "Angkor Thom"],
        "best_time": "November to March"
    },
    "Chichen Itza": {
        "description": "A Mayan city with iconic pyramids and ancient astronomical wonders.",
        "fun_facts": [
            "El Castillo pyramid aligns with equinoxes.",
            "Has a massive cenote used for sacrifices."
        ],
        "places_to_visit": ["El Castillo", "Great Ball Court", "Sacred Cenote", "Temple of the Warriors"],
        "best_time": "November to April"
    },
    "Kerala Backwaters": {
        "description": "A serene network of canals, lagoons, and houseboats in lush South India.",
        "fun_facts": [
            "Known as 'God’s Own Country.'",
            "A UNESCO-recognized biodiversity hotspot."
        ],
        "places_to_visit": ["Alleppey", "Kumarakom", "Vembanad Lake", "Kollam"],
        "best_time": "October to March"
    },
    "Jaipur": {
        "description": "The Pink City, famous for its royal palaces and vibrant markets.",
        "fun_facts": [
            "Painted pink in 1876 to welcome Prince Albert.",
            "Home to the world’s largest sundial."
        ],
        "places_to_visit": ["Hawa Mahal", "Amber Fort", "City Palace", "Jantar Mantar"],
        "best_time": "October to March"
    },
    "Ladakh": {
        "description": "A high-altitude desert with rugged landscapes and Buddhist monasteries.",
        "fun_facts": [
            "Known as 'Little Tibet.'",
            "Hosts the world’s highest motorable road."
        ],
        "places_to_visit": ["Pangong Lake", "Leh Palace", "Nubra Valley", "Hemis Monastery"],
        "best_time": "May to September"
    },
    "Varanasi": {
        "description": "India’s spiritual capital, with ancient ghats along the Ganges River.",
        "fun_facts": [
            "One of the world’s oldest inhabited cities.",
            "A major center for Hindu cremation rituals."
        ],
        "places_to_visit": ["Kashi Vishwanath Temple", "Dashashwamedh Ghat", "Sarnath", "Manikarnika Ghat"],
        "best_time": "October to March"
    },
    "Andaman Islands": {
        "description": "A tropical archipelago with pristine beaches and rich marine life.",
        "fun_facts": [
            "Home to the only active volcano in India.",
            "Once a British penal colony."
        ],
        "places_to_visit": ["Radhanagar Beach", "Cellular Jail", "Neil Island", "Ross Island"],
        "best_time": "October to May"
    },
    "Darjeeling": {
        "description": "A Himalayan hill station famed for tea gardens and stunning views.",
        "fun_facts": [
            "Produces some of the world’s finest tea.",
            "The Darjeeling Himalayan Railway is a UNESCO site."
        ],
        "places_to_visit": ["Tiger Hill", "Batasia Loop", "Tea Gardens", "Peace Pagoda"],
        "best_time": "March to May and October to November"
    },
    "Agra": {
        "description": "Home to the Taj Mahal, a timeless symbol of love and Mughal architecture.",
        "fun_facts": [
            "The Taj Mahal took 22 years to build.",
            "Agra Fort was once a walled city."
        ],
        "places_to_visit": ["Taj Mahal", "Agra Fort", "Itimad-ud-Daulah", "Mehtab Bagh"],
        "best_time": "October to March"
    },
    "Rishikesh": {
        "description": "The yoga capital of the world, nestled by the Ganges in the Himalayas.",
        "fun_facts": [
            "Visited by The Beatles in 1968.",
            "A hub for white-water rafting."
        ],
        "places_to_visit": ["Laxman Jhula", "Triveni Ghat", "Beatles Ashram", "Neer Garh Waterfall"],
        "best_time": "September to November and March to May"
    },
    "Mumbai": {
        "description": "India’s financial hub, with Bollywood glamour and colonial landmarks.",
        "fun_facts": [
            "The world’s most expensive home, Antilia, is here.",
            "Gateway of India was built in 1924."
        ],
        "places_to_visit": ["Gateway of India", "Marine Drive", "Elephanta Caves", "Chhatrapati Shivaji Terminus"],
        "best_time": "November to February"
    },
    "Udaipur": {
        "description": "The City of Lakes, with romantic palaces and serene waters.",
        "fun_facts": [
            "Known as the 'Venice of the East.'",
            "Lake Palace was a James Bond filming location."
        ],
        "places_to_visit": ["City Palace", "Lake Pichola", "Jag Mandir", "Saheliyon-ki-Bari"],
        "best_time": "October to March"
    },
    "Hampi": {
        "description": "A UNESCO site with ruins of a medieval kingdom amidst surreal landscapes.",
        "fun_facts": [
            "Once the world’s second-largest medieval city.",
            "Famous for its boulder-strewn terrain."
        ],
        "places_to_visit": ["Virupaksha Temple", "Vittala Temple", "Hampi Bazaar", "Matanga Hill"],
        "best_time": "October to February"
    },
    "Shimla": {
        "description": "A colonial hill station in the Himalayas with pine forests and charm.",
        "fun_facts": [
            "Was the summer capital of British India.",
            "The Kalka-Shimla Railway is a UNESCO site."
        ],
        "places_to_visit": ["The Ridge", "Mall Road", "Jakhoo Temple", "Christ Church"],
        "best_time": "March to June and December to February"
    },
    "Delhi": {
        "description": "India’s capital, blending ancient monuments with modern bustle.",
        "fun_facts": [
            "Has been rebuilt seven times in history.",
            "The Red Fort was the Mughal emperor’s palace."
        ],
        "places_to_visit": ["Red Fort", "Qutub Minar", "India Gate", "Lotus Temple"],
        "best_time": "October to March"
    },
    "Kanyakumari": {
        "description": "The southernmost tip of India, where three seas meet.",
        "fun_facts": [
            "Famous for its sunrise and sunset views.",
            "Home to the Vivekananda Rock Memorial."
        ],
        "places_to_visit": ["Vivekananda Rock", "Thiruvalluvar Statue", "Kanyakumari Beach", "Padmanabhapuram Palace"],
        "best_time": "October to March"
    },
    "Manali": {
        "description": "A beautiful hill station nestled in the Himalayas, perfect for nature and adventure lovers.",
        "fun_facts": [
            "A hotspot for honeymooners and trekkers.",
            "Home to one of the highest passes – Rohtang Pass."
        ],
        "places_to_visit": ["Solang Valley", "Hadimba Temple", "Old Manali", "Rohtang Pass"],
        "best_time": "October to February and March to June"
    },
    "Khajuraho": {
        "description": "A historic site famous for its erotic temple sculptures.",
        "fun_facts": [
            "A UNESCO World Heritage Site.",
            "Built between 950-1050 AD by the Chandela dynasty."
        ],
        "places_to_visit": ["Kandariya Mahadev Temple", "Lakshmana Temple", "Chaturbhuj Temple", "Javari Temple"],
        "best_time": "October to March"
    },
    "Pondicherry": {
        "description": "A charming coastal town with French colonial heritage and serene beaches.",
        "fun_facts": [
            "Also known as Puducherry.",
            "Auroville is an experimental township nearby."
        ],
        "places_to_visit": ["Auroville", "Promenade Beach", "Sri Aurobindo Ashram", "Paradise Beach"],
        "best_time": "October to March"
    },
    "Amritsar": {
        "description": "A spiritual city home to the magnificent Golden Temple.",
        "fun_facts": [
            "The Golden Temple feeds 100,000 people daily.",
            "Site of the Jallianwala Bagh massacre."
        ],
        "places_to_visit": ["Golden Temple", "Jallianwala Bagh", "Wagah Border", "Durgiana Temple"],
        "best_time": "October to March"
    },
    "Coorg": {
        "description": "A misty hill station in Karnataka, known for coffee and greenery.",
        "fun_facts": [
            "Called the 'Scotland of India.'",
            "A major coffee-producing region."
        ],
        "places_to_visit": ["Abbey Falls", "Raja’s Seat", "Madikeri Fort", "Talacauvery"],
        "best_time": "October to March"
    },
    "Jaisalmer": {
        "description": "The Golden City in the Thar Desert, with stunning forts and dunes.",
        "fun_facts": [
            "The fort is one of the few 'living forts' in the world.",
            "Famous for its desert camel safaris."
        ],
        "places_to_visit": ["Jaisalmer Fort", "Patwon Ki Haveli", "Sam Sand Dunes", "Gadisar Lake"],
        "best_time": "October to March"
    },
    "Kolkata": {
        "description": "A cultural hub with colonial architecture and vibrant festivals.",
        "fun_facts": [
            "India’s first capital under British rule.",
            "Hosts the massive Durga Puja festival."
        ],
        "places_to_visit": ["Victoria Memorial", "Howrah Bridge", "Dakshineswar Kali Temple", "Indian Museum"],
        "best_time": "October to March"
    },
    "Mysore": {
        "description": "A royal city known for its palace, silk, and sandalwood.",
        "fun_facts": [
            "Mysore Palace is lit with 100,000 bulbs during Dasara.",
            "Famous for its yoga heritage."
        ],
        "places_to_visit": ["Mysore Palace", "Chamundi Hill", "Brindavan Gardens", "St. Philomena’s Church"],
        "best_time": "October to February"
    },
    "Ooty": {
        "description": "A charming hill station in the Nilgiris with tea estates and lakes.",
        "fun_facts": [
            "Known as the 'Queen of Hills.'",
            "The Nilgiri Mountain Railway is a UNESCO site."
        ],
        "places_to_visit": ["Ooty Lake", "Botanical Gardens", "Doddabetta Peak", "Emerald Lake"],
        "best_time": "April to June and September to November"
    },
    "Rann of Kutch": {
        "description": "A vast salt desert hosting a unique festival and surreal landscapes.",
        "fun_facts": [
            "The world’s largest salt desert.",
            "Hosts the colorful Rann Utsav festival."
        ],
        "places_to_visit": ["Great Rann of Kutch", "Dholavira", "Kala Dungar", "Bhuj"],
        "best_time": "November to February"
    },
    "Hyderabad": {
        "description": "A city of pearls, biryani, and historic Golconda Fort.",
        "fun_facts": [
            "Once the richest princely state in India.",
            "Famous for its Charminar monument."
        ],
        "places_to_visit": ["Charminar", "Golconda Fort", "Hussain Sagar Lake", "Qutb Shahi Tombs"],
        "best_time": "October to February"
    },
    "Srinagar": {
        "description": "A paradise in Kashmir with serene lakes and Mughal gardens.",
        "fun_facts": [
            "Known as the 'Venice of the East' for its houseboats.",
            "Famous for its floating gardens."
        ],
        "places_to_visit": ["Dal Lake", "Shalimar Bagh", "Shankaracharya Temple", "Pari Mahal"],
        "best_time": "April to October"
    },
    "Ajanta Caves": {
        "description": "Ancient rock-cut caves with Buddhist art and sculptures.",
        "fun_facts": [
            "A UNESCO World Heritage Site.",
            "Date back to the 2nd century BC."
        ],
        "places_to_visit": ["Ajanta Caves", "Viewpoint", "Aurangabad", "Ellora Caves (nearby)"],
        "best_time": "October to March"
    },
    "Chennai": {
        "description": "A coastal city with temples, beaches, and a rich cultural heritage.",
        "fun_facts": [
            "India’s first British fort was built here.",
            "Known as the 'Detroit of India' for its auto industry."
        ],
        "places_to_visit": ["Marina Beach", "Kapaleeshwarar Temple", "Fort St. George", "Elliot’s Beach"],
        "best_time": "November to February"
    },
    "Gangtok": {
        "description": "A Himalayan town with monasteries and stunning Kanchenjunga views.",
        "fun_facts": [
            "India’s first fully organic state.",
            "Home to the world’s third-highest peak."
        ],
        "places_to_visit": ["Rumtek Monastery", "Nathula Pass", "Enchey Monastery", "Tsomgo Lake"],
        "best_time": "March to June and September to November"
    },
    "Madurai": {
        "description": "An ancient city famous for the Meenakshi Temple and vibrant streets.",
        "fun_facts": [
            "Known as the 'Athens of the East.'",
            "Over 2,500 years old."
        ],
        "places_to_visit": ["Meenakshi Temple", "Thirumalai Nayakkar Palace", "Vaigai River", "Alagar Kovil"],
        "best_time": "October to March"
    },
    "Diu": {
        "description": "A quiet island with Portuguese charm and serene beaches.",
        "fun_facts": [
            "Was a Portuguese colony until 1961.",
            "Famous for its historic fort."
        ],
        "places_to_visit": ["Diu Fort", "Naida Caves", "Nagoa Beach", "St. Paul’s Church"],
        "best_time": "October to March"
    },
    "Nainital": {
        "description": "A picturesque lake town in the Kumaon hills of Uttarakhand.",
        "fun_facts": [
            "Shaped like an eye, Naini Lake is its centerpiece.",
            "A popular colonial-era retreat."
        ],
        "places_to_visit": ["Naini Lake", "Naina Devi Temple", "Snow View Point", "Tiffin Top"],
        "best_time": "March to June and September to November"
    },
    "Bhopal": {
        "description": "A city of lakes with historic sites and natural beauty.",
        "fun_facts": [
            "Known as the 'City of Lakes.'",
            "Home to one of India’s largest mosques."
        ],
        "places_to_visit": ["Upper Lake", "Taj-ul-Masajid", "Bhimbetka Rock Shelters", "Van Vihar"],
        "best_time": "October to March"
    },
    "Ellora Caves": {
        "description": "A UNESCO site with rock-cut temples from multiple religions.",
        "fun_facts": [
            "Features Hindu, Buddhist, and Jain caves.",
            "The Kailasa Temple is carved from a single rock."
        ],
        "places_to_visit": ["Kailasa Temple", "Cave 16", "Aurangabad", "Ajanta Caves (nearby)"],
        "best_time": "October to March"
    },
    "Puri": {
        "description": "A coastal pilgrimage town with the famous Jagannath Temple.",
        "fun_facts": [
            "Hosts the massive Rath Yatra festival.",
            "One of India’s four holy dhams."
        ],
        "places_to_visit": ["Jagannath Temple", "Puri Beach", "Konark Sun Temple (nearby)", "Chilika Lake"],
        "best_time": "October to March"
    },
    "Auli": {
        "description": "A Himalayan skiing destination with snowy slopes and oak forests.",
        "fun_facts": [
            "One of India’s top ski resorts.",
            "Offers views of Nanda Devi peak."
        ],
        "places_to_visit": ["Auli Ski Resort", "Joshimath", "Gorson Bugyal", "Chenab Lake"],
        "best_time": "December to March"
    },
    "Ahmedabad": {
        "description": "A bustling city with historic architecture and textile heritage.",
        "fun_facts": [
            "India’s first UNESCO World Heritage City.",
            "Famous for its kite festival."
        ],
        "places_to_visit": ["Sabarmati Ashram", "Jama Masjid", "Sidi Saiyyed Mosque", "Kankaria Lake"],
        "best_time": "October to March"
    },
    "Konark": {
        "description": "Home to the Sun Temple, a masterpiece of ancient architecture.",
        "fun_facts": [
            "A UNESCO World Heritage Site.",
            "Designed as a chariot with 24 wheels."
        ],
        "places_to_visit": ["Sun Temple", "Konark Beach", "Chandrabhaga Beach", "Arka Teertha"],
        "best_time": "October to March"
    },
    "Munnar": {
        "description": "A lush hill station with rolling tea plantations and misty peaks.",
        "fun_facts": [
            "Home to the rare Neelakurinji flower.",
            "A major tea-producing region."
        ],
        "places_to_visit": ["Tea Gardens", "Eravikulam National Park", "Mattupetty Dam", "Anamudi Peak"],
        "best_time": "September to March"
    },
    "Bhubaneswar": {
        "description": "The Temple City of India, with ancient shrines and modern charm.",
        "fun_facts": [
            "Known as the 'City of Temples.'",
            "Once had over 7,000 temples."
        ],
        "places_to_visit": ["Lingaraj Temple", "Udayagiri Caves", "Dhauli Hill", "Nandankanan Zoo"],
        "best_time": "October to March"
    },
    "Gulmarg": {
        "description": "A snowy paradise in Kashmir, famous for skiing and gondola rides.",
        "fun_facts": [
            "Hosts Asia’s highest cable car.",
            "A popular Bollywood filming location."
        ],
        "places_to_visit": ["Gulmarg Gondola", "Apharwat Peak", "St. Mary’s Church", "Alpather Lake"],
        "best_time": "December to March"
    },
    "Jodhpur": {
        "description": "The Blue City, with a majestic fort and desert landscapes.",
        "fun_facts": [
            "Houses are painted blue to repel insects.",
            "Mehrangarh Fort is one of India’s largest."
        ],
        "places_to_visit": ["Mehrangarh Fort", "Jaswant Thada", "Umaid Bhawan Palace", "Mandore Gardens"],
        "best_time": "October to March"
    },
    "Leh": {
        "description": "A high-altitude desert town with monasteries and rugged beauty.",
        "fun_facts": [
            "Known as the 'Land of High Passes.'",
            "The coldest inhabited place in India."
        ],
        "places_to_visit": ["Leh Palace", "Shanti Stupa", "Magnetic Hill", "Thiksey Monastery"],
        "best_time": "May to September"
    },
    "Kodaikanal": {
        "description": "A misty hill station with lakes, waterfalls, and pine forests.",
        "fun_facts": [
            "Known as the 'Princess of Hill Stations.'",
            "Famous for its homemade chocolates."
        ],
        "places_to_visit": ["Kodaikanal Lake", "Coaker’s Walk", "Pillar Rocks", "Bear Shola Falls"],
        "best_time": "April to June and September to November"
    },
    "Gokarna": {
        "description": "A tranquil beach town with spiritual significance and sandy shores.",
        "fun_facts": [
            "A quieter alternative to Goa.",
            "Home to the sacred Mahabaleshwar Temple."
        ],
        "places_to_visit": ["Om Beach", "Kudle Beach", "Mahabaleshwar Temple", "Half Moon Beach"],
        "best_time": "October to March"
    },
    "Tirupati": {
        "description": "A major pilgrimage site with the revered Tirumala Venkateswara Temple.",
        "fun_facts": [
            "One of the richest temples in the world.",
            "Receives millions of pilgrims annually."
        ],
        "places_to_visit": ["Tirumala Temple", "Sri Kapileswara Swamy Temple", "Talakona Waterfalls", "Chandragiri Fort"],
        "best_time": "September to March"
    },
    "Shillong": {
        "description": "The Scotland of the East, with rolling hills and waterfalls.",
        "fun_facts": [
            "Known for its music scene.",
            "Receives heavy rainfall, like nearby Cherrapunji."
        ],
        "places_to_visit": ["Umiam Lake", "Elephant Falls", "Shillong Peak", "Ward’s Lake"],
        "best_time": "March to June and September to November"
    },
    "Sundarbans": {
        "description": "A vast mangrove forest and home to the Royal Bengal Tiger.",
        "fun_facts": [
            "The world’s largest delta region.",
            "A UNESCO World Heritage Site."
        ],
        "places_to_visit": ["Sundarbans National Park", "Sajnekhali Watch Tower", "Sudhanyakhali", "Netidhopani"],
        "best_time": "September to March"
    },
    "Bikaner": {
        "description": "A desert city with grand forts and a unique rat temple.",
        "fun_facts": [
            "Home to the Karni Mata Temple with 25,000 rats.",
            "Famous for its camel festival."
        ],
        "places_to_visit": ["Junagarh Fort", "Karni Mata Temple", "Lalgarh Palace", "Rampuria Haveli"],
        "best_time": "October to March"
    },
    "Haridwar": {
        "description": "A holy city on the Ganges, famous for its evening Ganga Aarti.",
        "fun_facts": [
            "One of the seven holiest places in Hinduism.",
            "Hosts the Kumbh Mela every 12 years."
        ],
        "places_to_visit": ["Har Ki Pauri", "Mansa Devi Temple", "Chandi Devi Temple", "Rajaji National Park"],
        "best_time": "October to March"
    },
    "Tawang": {
        "description": "A remote Himalayan town with a large monastery and stunning views.",
        "fun_facts": [
            "Home to India’s largest Buddhist monastery.",
            "Near the India-China border."
        ],
        "places_to_visit": ["Tawang Monastery", "Sela Pass", "Madhuri Lake", "Nuranang Falls"],
        "best_time": "March to June and September to October"
    },
    "Alleppey": {
        "description": "The Venice of the East, famous for backwaters and houseboat cruises.",
        "fun_facts": [
            "Hosts the Nehru Trophy Boat Race.",
            "Known for its coir industry."
        ],
        "places_to_visit": ["Alleppey Backwaters", "Marari Beach", "Krishnapuram Palace", "Pathiramanal Island"],
        "best_time": "November to February"
    },
    "Pushkar": {
        "description": "A sacred town with a holy lake and a famous camel fair.",
        "fun_facts": [
            "One of the oldest cities in India.",
            "The only temple dedicated to Lord Brahma is here."
        ],
        "places_to_visit": ["Pushkar Lake", "Brahma Temple", "Savitri Temple", "Pushkar Camel Fair"],
        "best_time": "October to March"
    },
    "Dharamshala": {
        "description": "A Himalayan retreat, home to the Dalai Lama and Tibetan culture.",
        "fun_facts": [
            "McLeod Ganj is called 'Little Lhasa.'",
            "A hub for trekking and paragliding."
        ],
        "places_to_visit": ["McLeod Ganj", "Dalai Lama Temple", "Bhagsu Waterfall", "Triund"],
        "best_time": "March to June and September to November"
    },
    "Lucknow": {
        "description": "The City of Nawabs, famous for kebabs and intricate architecture.",
        "fun_facts": [
            "Known for its chikankari embroidery.",
            "The Bara Imambara has a famous labyrinth."
        ],
        "places_to_visit": ["Bara Imambara", "Chota Imambara", "Rumi Darwaza", "Hazratganj"],
        "best_time": "October to March"
    },
    "Mahabalipuram": {
        "description": "A coastal town with ancient rock-cut temples and beaches.",
        "fun_facts": [
            "A UNESCO World Heritage Site.",
            "Famous for its Shore Temple."
        ],
        "places_to_visit": ["Shore Temple", "Pancha Rathas", "Arjuna’s Penance", "Mahabalipuram Beach"],
        "best_time": "October to March"
    },
    "Mussoorie": {
        "description": "The Queen of Hills, with scenic views and colonial charm.",
        "fun_facts": [
            "A popular honeymoon destination.",
            "Home to India’s oldest tavern, Ruskin Bond’s haunt."
        ],
        "places_to_visit": ["Kempty Falls", "Gun Hill", "Lal Tibba", "Camel’s Back Road"],
        "best_time": "March to June and September to November"
    },
    "Guwahati": {
        "description": "The gateway to Northeast India, with temples and the Brahmaputra River.",
        "fun_facts": [
            "Home to the ancient Kamakhya Temple.",
            "A major tea auction center."
        ],
        "places_to_visit": ["Kamakhya Temple", "Umananda Island", "Assam State Museum", "Pobitora Wildlife Sanctuary"],
        "best_time": "October to April"
    },
    "Sanchi": {
        "description": "A historic site with ancient Buddhist stupas and monasteries.",
        "fun_facts": [
            "A UNESCO World Heritage Site.",
            "The Great Stupa dates back to Emperor Ashoka."
        ],
        "places_to_visit": ["Great Stupa", "Sanchi Museum", "Ashoka Pillar", "Torana Gateway"],
        "best_time": "October to March"
    },
    "Varkala": {
        "description": "A cliffside beach town with springs and a laid-back vibe.",
        "fun_facts": [
            "Known for its natural mineral springs.",
            "A quieter alternative to Kovalam."
        ],
        "places_to_visit": ["Varkala Beach", "Janardhana Swamy Temple", "Kappil Lake", "Sivagiri Mutt"],
        "best_time": "October to March"
    },
    "Pune": {
        "description": "A vibrant city blending history, education, and modernity.",
        "fun_facts": [
            "Known as the 'Oxford of the East.'",
            "Once the seat of the Maratha Empire."
        ],
        "places_to_visit": ["Shaniwar Wada", "Aga Khan Palace", "Sinhagad Fort", "Osho Ashram"],
        "best_time": "October to February"
    },
    "Kaziranga": {
        "description": "A wildlife haven famous for the one-horned rhinoceros.",
        "fun_facts": [
            "A UNESCO World Heritage Site.",
            "Hosts two-thirds of the world’s one-horned rhinos."
        ],
        "places_to_visit": ["Kaziranga National Park", "Orchid Park", "Kohora", "Bagori Range"],
        "best_time": "November to April"
    },
    "Badami": {
        "description": "A historic town with rock-cut caves and ancient temples.",
        "fun_facts": [
            "Capital of the Chalukya dynasty in the 6th century.",
            "Known for its red sandstone cliffs."
        ],
        "places_to_visit": ["Badami Caves", "Agastya Lake", "Bhutanatha Temple", "Malegitti Shivalaya"],
        "best_time": "October to March"
    },
    "Cherrapunji": {
        "description": "One of the wettest places on Earth, with waterfalls and living root bridges.",
        "fun_facts": [
            "Once held the record for the most rainfall in a year.",
            "Also known as Sohra."
        ],
        "places_to_visit": ["Nohkalikai Falls", "Living Root Bridges", "Mawsmai Cave", "Seven Sisters Falls"],
        "best_time": "October to May"
    },
    "Nagpur": {
        "description": "The orange city with lakes, wildlife, and historic sites.",
        "fun_facts": [
            "Known as the 'Orange Capital of India.'",
            "Located at the exact center of India."
        ],
        "places_to_visit": ["Deekshabhoomi", "Tadoba National Park", "Ramdham", "Ambazari Lake"],
        "best_time": "October to March"
    },
    "Thanjavur": {
        "description": "A cultural hub famous for the Brihadeeswarar Temple and Tanjore paintings.",
        "fun_facts": [
            "A UNESCO World Heritage Site.",
            "Known as the 'Rice Bowl of Tamil Nadu.'"
        ],
        "places_to_visit": ["Brihadeeswarar Temple", "Thanjavur Palace", "Gangaikonda Cholapuram", "Schwartz Church"],
        "best_time": "October to March"
    },
    "Lonavala": {
        "description": "A popular hill station with waterfalls, caves, and lush greenery.",
        "fun_facts": [
            "Famous for its chikki (a sweet snack).",
            "A monsoon getaway near Mumbai."
        ],
        "places_to_visit": ["Rajmachi Fort", "Lohagad Fort", "Bhushi Dam", "Tiger’s Leap"],
        "best_time": "June to September and October to March"
    },
    "Kochi": {
        "description": "A port city with colonial history, backwaters, and Chinese fishing nets.",
        "fun_facts": [
            "Known as the 'Queen of the Arabian Sea.'",
            "India’s first European settlement."
        ],
        "places_to_visit": ["Fort Kochi", "Mattancherry Palace", "Chinese Fishing Nets", "Jew Town"],
        "best_time": "October to March"
    },
    "Gir Forest": {
        "description": "The last refuge of the Asiatic lion, a wildlife paradise.",
        "fun_facts": [
            "A UNESCO tentative list site.",
            "The only place outside Africa to see lions in the wild."
        ],
        "places_to_visit": ["Gir National Park", "Devalia Safari Park", "Kamleshwar Dam", "Kankai Mata Temple"],
        "best_time": "December to March"
    },
    "Bodh Gaya": {
        "description": "The site where Buddha attained enlightenment, a spiritual haven.",
        "fun_facts": [
            "The Mahabodhi Tree is a direct descendant of the original.",
            "A UNESCO World Heritage Site."
        ],
        "places_to_visit": ["Mahabodhi Temple", "Bodhi Tree", "Great Buddha Statue", "Sujata Stupa"],
        "best_time": "October to March"
    },
    "Mandu": {
        "description": "A ruined hilltop fortress with palaces and romantic monsoon views.",
        "fun_facts": [
            "Known as the 'City of Joy' in medieval times.",
            "Famous for the love story of Baz Bahadur and Rani Roopmati."
        ],
        "places_to_visit": ["Jahaz Mahal", "Rani Roopmati Pavilion", "Hindola Mahal", "Baz Bahadur’s Palace"],
        "best_time": "July to February"
    },
    "Dalhousie": {
        "description": "A colonial hill station with pine forests and Himalayan vistas.",
        "fun_facts": [
            "Named after Lord Dalhousie, a British governor.",
            "A quiet alternative to Shimla."
        ],
        "places_to_visit": ["Khajjiar", "Panchpula", "St. John’s Church", "Dainkund Peak"],
        "best_time": "March to June and September to November"
    },
    "Daman": {
        "description": "A coastal retreat with Portuguese heritage and sandy beaches.",
        "fun_facts": [
            "Was a Portuguese enclave until 1961.",
            "Known for its quiet, laid-back vibe."
        ],
        "places_to_visit": ["Devka Beach", "Nani Daman Fort", "Jampore Beach", "St. Jerome Fort"],
        "best_time": "October to March"
    },
    "Patnitop": {
        "description": "A snowy hill station in Jammu with pine forests and adventure trails.",
        "fun_facts": [
            "A lesser-known gem in the Himalayas.",
            "Offers paragliding and skiing."
        ],
        "places_to_visit": ["Nathatop", "Sanasar", "Patnitop Park", "Shiva Garh"],
        "best_time": "December to March"
    },
    "Ranthambore": {
        "description": "A tiger reserve with historic forts and rich wildlife.",
        "fun_facts": [
            "Once a royal hunting ground.",
            "One of India’s best places to spot tigers."
        ],
        "places_to_visit": ["Ranthambore National Park", "Ranthambore Fort", "Padam Talao", "Trinetra Ganesh Temple"],
        "best_time": "October to April"
    },
    "Gwalior": {
        "description": "A historic city with a grand hilltop fort and musical heritage.",
        "fun_facts": [
            "Birthplace of the legendary musician Tansen.",
            "The Gwalior Fort dates back to the 8th century."
        ],
        "places_to_visit": ["Gwalior Fort", "Jai Vilas Palace", "Tansen Tomb", "Sun Temple"],
        "best_time": "October to March"
    },
    "Mount Abu": {
        "description": "Rajasthan’s only hill station, with lakes and Jain temples.",
        "fun_facts": [
            "Home to the famous Dilwara Jain Temples.",
            "The highest peak in the Aravalli Range."
        ],
        "places_to_visit": ["Nakki Lake", "Dilwara Temples", "Guru Shikhar", "Sunset Point"],
        "best_time": "October to March"
    },
    "Velankanni": {
        "description": "A coastal pilgrimage site with a grand basilica and serene beaches.",
        "fun_facts": [
            "Known as the 'Lourdes of the East.'",
            "The basilica is shaped like a cross."
        ],
        "places_to_visit": ["Basilica of Our Lady of Good Health", "Velankanni Beach", "Church Museum", "Nagapattinam"],
        "best_time": "October to March"
    },
    "Periyar": {
        "description": "A wildlife sanctuary with a scenic lake and spice plantations.",
        "fun_facts": [
            "Famous for its elephant and tiger sightings.",
            "The Periyar River feeds the sanctuary."
        ],
        "places_to_visit": ["Periyar National Park", "Thekkady", "Periyar Lake", "Mangala Devi Temple"],
        "best_time": "October to February"
    },
    "Orchha": {
        "description": "A medieval town with palaces, temples, and a serene riverside.",
        "fun_facts": [
            "Known for its Bundela architecture.",
            "Once the capital of the Bundela Rajputs."
        ],
        "places_to_visit": ["Orchha Fort", "Chaturbhuj Temple", "Raja Mahal", "Betwa River"],
        "best_time": "October to March"
    },
    "Chandigarh": {
        "description": "A planned city with modern design, gardens, and a unique charm.",
        "fun_facts": [
            "Designed by Le Corbusier.",
            "India’s first planned city post-independence."
        ],
        "places_to_visit": ["Rock Garden", "Sukhna Lake", "Rose Garden", "Capitol Complex"],
        "best_time": "October to March"
    },
    "Kutch": {
        "description": "A vast desert region with handicrafts and the Great Rann festival.",
        "fun_facts": [
            "The Rann turns into a white salt desert in winter.",
            "Home to the ancient Dholavira site."
        ],
        "places_to_visit": ["Great Rann of Kutch", "Dholavira", "Bhuj", "Mandvi Beach"],
        "best_time": "November to February"
    },
    "Spiti Valley": {
        "description": "A cold desert valley with ancient monasteries and stark beauty.",
        "fun_facts": [
            "Known as 'Little Tibet.'",
            "Hosts the world’s highest post office."
        ],
        "places_to_visit": ["Key Monastery", "Tabo Monastery", "Dhankar Lake", "Pin Valley"],
        "best_time": "May to October"
    },
    "Hazaribagh": {
        "description": "A forested region with waterfalls and wildlife sanctuaries.",
        "fun_facts": [
            "Name means 'thousand gardens.'",
            "A lesser-known gem in Jharkhand."
        ],
        "places_to_visit": ["Hazaribagh National Park", "Canary Hill", "Tilaiya Dam", "Konar Dam"],
        "best_time": "October to March"
    },
    "Warangal": {
        "description": "A historic city with ancient temples and forts from the Kakatiya dynasty.",
        "fun_facts": [
            "Known for its Thousand Pillar Temple.",
            "Once a major Telugu cultural center."
        ],
        "places_to_visit": ["Warangal Fort", "Thousand Pillar Temple", "Bhadrakali Temple", "Pakhal Lake"],
        "best_time": "October to March"
    },
    "Kalimpong": {
        "description": "A quiet hill town with monasteries and Himalayan views.",
        "fun_facts": [
            "Famous for its flower nurseries.",
            "A trade hub between India and Tibet historically."
        ],
        "places_to_visit": ["Zang Dhok Palri Monastery", "Deolo Hill", "Durpin Dara Hill", "Thongsa Gompa"],
        "best_time": "March to June and September to November"
    },
    "Jabalpur": {
        "description": "A city known for marble rocks and cascading waterfalls.",
        "fun_facts": [
            "The Dhuandhar Falls create a misty smoke effect.",
            "A major military base during British rule."
        ],
        "places_to_visit": ["Bhedaghat", "Dhuandhar Falls", "Marble Rocks", "Madan Mahal Fort"],
        "best_time": "October to March"
    },
    "Dwarka": {
        "description": "An ancient city tied to Lord Krishna, with temples and beaches.",
        "fun_facts": [
            "Believed to be Krishna’s kingdom.",
            "One of the four sacred Hindu pilgrimage sites."
        ],
        "places_to_visit": ["Dwarkadhish Temple", "Bet Dwarka", "Nageshwar Jyotirlinga", "Gomti Ghat"],
        "best_time": "October to March"
    },
    "Panchgani": {
        "description": "A hill station with strawberry farms and colonial charm.",
        "fun_facts": [
            "Known for its boarding schools.",
            "Offers stunning views of the Krishna Valley."
        ],
        "places_to_visit": ["Table Land", "Sydney Point", "Parsi Point", "Rajpuri Caves"],
        "best_time": "September to May"
    },
    "Kanpur": {
        "description": "An industrial city with historic sites and the Ganges River.",
        "fun_facts": [
            "Known as the 'Manchester of the East.'",
            "A key center during the 1857 uprising."
        ],
        "places_to_visit": ["JK Temple", "Allen Forest Zoo", "Bithoor", "Kanpur Memorial Church"],
        "best_time": "October to March"
    },
    "Bastar": {
        "description": "A tribal region with forests, waterfalls, and rich culture.",
        "fun_facts": [
            "Famous for its Bastar Dussehra festival.",
            "Home to unique tribal art like bell metal."
        ],
        "places_to_visit": ["Chitrakote Falls", "Kanger Valley National Park", "Danteshwari Temple", "Bastar Palace"],
        "best_time": "October to March"
    },
    "Sarnath": {
        "description": "A Buddhist pilgrimage site where Buddha gave his first sermon.",
        "fun_facts": [
            "The Ashoka Pillar here is India’s national emblem.",
            "A UNESCO tentative list site."
        ],
        "places_to_visit": ["Dhamek Stupa", "Sarnath Museum", "Chaukhandi Stupa", "Mulagandha Kuti Vihar"],
        "best_time": "October to March"
    },
    "Agartala": {
        "description": "A cultural hub in Northeast India with palaces and temples.",
        "fun_facts": [
            "Home to the royal Ujjayanta Palace.",
            "A gateway to the Tripura Sundari Temple."
        ],
        "places_to_visit": ["Ujjayanta Palace", "Neermahal", "Tripura Sundari Temple", "Unakoti"],
        "best_time": "October to April"
    },
    "Chittorgarh": {
        "description": "A historic fort with tales of valor and Rajput architecture.",
        "fun_facts": [
            "India’s largest fort by area.",
            "Famous for the story of Rani Padmini."
        ],
        "places_to_visit": ["Chittorgarh Fort", "Vijay Stambh", "Kirti Stambh", "Padmini Palace"],
        "best_time": "October to March"
    },
    "Almora": {
        "description": "A peaceful Himalayan town with pine forests and ancient temples.",
        "fun_facts": [
            "Known for its Kumaoni culture.",
            "Offers panoramic views of the Himalayas."
        ],
        "places_to_visit": ["Bright End Corner", "Kasar Devi Temple", "Binsar Wildlife Sanctuary", "Zero Point"],
        "best_time": "April to June and September to November"
    },
    "Bundi": {
        "description": "A small town with forts, stepwells, and a rich Rajput legacy.",
        "fun_facts": [
            "Famous for its intricate miniature paintings.",
            "The Taragarh Fort offers stunning views."
        ],
        "places_to_visit": ["Taragarh Fort", "Rani Ji Ki Baori", "Sukh Mahal", "Garh Palace"],
        "best_time": "October to March"
    }
}

# Perform updates
for name, data in updates.items():
    result = collection.update_one(
        {"name": name},
        {"$set": data}
    )
    if result.matched_count == 0:
        print(f"Warning: No match found for {name}. Ensure the destination exists in the collection.")

print("Destination entries updated successfully.")