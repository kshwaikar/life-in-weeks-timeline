# life-in-weeks-timeline

# 📅 Life in Weeks Timeline Web App

A powerful, visual representation of a person’s life in weeks — from birth until now — with interactive options to mark important personal events and display global milestones.

---

## 🌟 Features

- ✅ User Registration (Name, Birthdate, Email, Password)
- ✅ Weekly Grid showing all lived weeks
- ✅ Personal Event Functionality:
  - Add events with title, date, and week
  - Edit & Delete supported (fully functional)
  - Blue color-coded dots with hover tooltip
- ❌ Global Events from CSV not integrated (planned, but skipped)
- ✅ Backend: RESTful APIs using Flask + MySQL
- ✅ Frontend: HTML, CSS, and JS — all in a single `index.html`
- ⚙️ Full frontend-backend integration tested and working

---

## 🧠 Tech Stack

**Frontend:**
- HTML5 + CSS3 (custom styled)
- Vanilla JavaScript

**Backend:**
- Python Flask (RESTful API)
- MySQL
- JSON (for global events file)

---

## 📁 Project Structure

project-root/
│
├── index.html # Frontend (HTML + CSS + JS)
├── app.py # Flask backend
├── Database/
│ └── weeks.sql # MySQL schema
├── static/
│ └── Global Events.json # (used, but not loaded due to CSV issue)
└── README.md # You're reading it!


---

## 🔧 API Routes (Backend)

- `POST /api/register` → Register a new user
- `POST /api/events` → Add a personal event
- `GET /api/events/<user_id>` → Get user's events
- `PUT /api/events/<event_id>` → Edit personal event ✅
- `DELETE /api/events/<event_id>` → Delete personal event ✅

---

## ⚠️ Known Limitations

- ❌ Global Events from CSV didn’t render (planned, but skipped for submission)
- ❌ No login/authentication system
- ✅ CRUD operations for **personal events** are all working perfectly
- 🔄 Global events file (`Global Events.json`) is present but not parsed in frontend due to integration issue

---

## 🖼️ UI Overview

- Each square = 1 week of life lived
- Blue Dot = Personal Event
- Hover Tooltip = Event Title & Date

---

## 📦 How to Run Locally

1. Clone the repo  
   `git clone https://github.com/<your-username>/<repo-name>.git`

2. Navigate into project  
   `cd <repo-name>`

3. (Optional) Setup virtual environment  
   `python -m venv venv && source venv/bin/activate` *(or on Windows: `venv\Scripts\activate`)*

4. Install required packages  
   `pip install flask mysql-connector-python`

5. Run the app  
   `python app.py`

---

## 👨‍💻 Created By

Kshitij Waikar
Jayashree Srivastava
Akash Baghrecha


 

