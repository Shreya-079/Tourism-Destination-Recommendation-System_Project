
<p align="center">
  <a href="screenshots/demo.mp4">
    <img src="screenshots/ss-demo.png" width="700">
  </a>
</p>

# Tourism Recommender System

A full-stack travel recommendation web application built using **Flask** and **MongoDB**.  
The system provides personalized destination suggestions based on user preferences and includes authentication, detailed destination insights, and a review mechanism.

---

## Overview

The Tourism Recommender System is designed to enhance travel discovery through a preference-based recommendation engine. It integrates a dynamic frontend with a structured backend and NoSQL database to deliver customized travel suggestions and interactive destination details.

This project demonstrates practical implementation of:

- Full-stack web development  
- RESTful routing with Flask  
- NoSQL database integration (MongoDB)  
- Session-based authentication  
- CRUD operations  
- Dynamic content rendering using Jinja2  

---

## Key Features

### 1. Personalized Recommendations
Users receive destination suggestions based on selected interests such as beaches, rivers, food, or adventure.

### 2. User Authentication
- Secure signup and login system  
- Session-based access control  
- Separate storage for authentication and user profile data


<p align="center">
  <img src="screenshots/login.png" width="45%" />
  <img src="screenshots/signup.png" width="45%" />
</p>


### 3. Destination Detail Pages
Each destination includes:
- Description  
- Fun facts  
- Places to visit  
- Best time to visit  
- Integrated Google Maps view  


<p align="center">
  <img src="screenshots/desc.png" width="45%" />
  <img src="screenshots/detail1.png" width="45%" />
</p>


### 4. Review & Rating System
- Users can submit reviews  
- Average ratings are dynamically calculated  
- All reviews are displayed on the destination page  


<p align="center">
  <img src="screenshots/detail2.png" width="700">
</p>

---

## Tech Stack

**Backend**
- Python  
- Flask  

**Database**
- MongoDB (PyMongo)  

**Frontend**
- HTML5  
- CSS3  
- Jinja2 Templates  

**Other Tools**
- VS Code  
- Git & GitHub  

---

## Project Structure

```bash
tourism-recommender-system/
│
├── app.py
├── populate_unique_destinations.py
├── templates/
├── static/
├── requirements.txt
└── README.md
```

- `app.py` – Core Flask application and route handling  
- `populate_unique_destinations.py` – Script to seed database with destinations  
- `templates/` – HTML templates  
- `static/` – CSS, images, and frontend assets  
- `requirements.txt` – Python dependencies  

---

## Installation & Setup

### Step 1: Clone the Repository

```bash

git clone https://github.com/Shreya-079/Tourism-Destination-Recommendation-System_Project.git
cd tourism-recommender-system
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure MongoDB

Ensure MongoDB is running locally:

```bash
mongodb://localhost:27017
```

Seed the database:

```bash
python populate_unique_destinations.py
```

### Step 4: Run the Application

```bash
python app.py
```

Open in browser:

```bash
http://127.0.0.1:5000/
```

---

## Learning Outcomes

- Built scalable Flask backend  
- Integrated MongoDB for data management  
- Implemented authentication & session handling  
- Designed dynamic frontend architecture  

---

## Future Enhancements

- AI-based recommendation engine  
- Cloud deployment  
- Travel analytics dashboard  
- Admin control panel  

