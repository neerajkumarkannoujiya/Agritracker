# 🌾 AgriTracker

**Version**: 1.0  
**Prepared by**: Neeraj Ku. Kannoujiya, Aman Sahu  
**Approved by**: Dr. Gaurav Srivastava  
**Date**: 06/04/2025  

---

## 📌 Overview

**AgriTracker** is a web-based agricultural management and marketplace platform built specifically for **Large and Mid-scale farmers in India**. It offers digital farm record-keeping, a direct-to-buyer marketplace, and a blog-based knowledge-sharing community for farmers. 

It aims to bridge gaps in data management, reduce dependence on middlemen, and enhance sustainability in Indian agriculture.

---

## 🧠 Purpose

This repository hosts the source code and configuration for the **AgriTracker** platform. It includes:

- Backend & API development using Django REST Framework  
- A responsive frontend using Bootstrap and Django templates  
- PostgreSQL integration for encrypted farm data storage  
- Marketplace functionality for connecting farmers and buyers  
- A blog for agricultural knowledge exchange  

---

## 🎯 Objectives

| Objective             | Description                                     | Success Metric                        |
|-----------------------|-------------------------------------------------|---------------------------------------|
| Data-Driven Decisions | Record and analyze farm operations              | 80% adoption rate in pilot testing    |
| Market Linkage        | Enable direct farmer-to-buyer connections       | 50% reduction in middlemen dependency |
| Sustainability        | Promote efficient resource usage                | 30% increase in water/fertilizer efficiency |

---

## 🧩 Features

### ✅ Phase 1 (In Scope)
- 👨‍🌾 **Farm Management**
  - Crop cycle & season tracking
  - Resource input logging (e.g., water, fertilizers)
  - Auto-generated reports (PDF/Excel)

- 🛒 **Marketplace**
  - Farmers can list products (type, quantity, price)
  - Buyers can search and filter listings
  - Communication via WhatsApp or phone

- 📝 **Blog & Knowledge Sharing**
  - Publish experiences and farming techniques
  - Share profit/loss case studies
  - Recommend pesticides and insecticides
    ![Dashboard Screenshot](dashboard.jpeg)  

### 🚫 Out of Scope (Future Phases)
- Online payment integration  
- AI/ML-driven analytics and predictive insights  

---

## 👥 Intended Audience

| Role                 | Usage Purpose                     |
|----------------------|-----------------------------------|
| Developers           | System architecture, implementation |
| Testers              | Validation, bug fixing            |
| Project Managers     | Timeline/resource tracking        |
| Farmers (End Users)  | Day-to-day platform usage         |
| Agricultural Orgs    | Impact evaluation & feedback      |

---

## 🛠️ Tech Stack

| Layer      | Technology                                |
|------------|--------------------------------------------|
| Frontend   | HTML5, CSS3, Bootstrap, JavaScript         |
| Backend    | Python 3.x, Django, Django REST Framework  |
| Database   | PostgreSQL (with encryption)               |
| Testing    | PyTest, UAT (User Acceptance Testing)      |
| Deployment | Linux-based servers, Phase-wise rollout    |

---

## 🌀 Development Methodology

AgriTracker follows the **Agile** model with iterative development cycles:

1. **Requirement Gathering**  
   - Surveys & interviews with 100+ farmers across 5 Indian states  
2. **Prototyping**  
   - Low-fidelity UI mockups and feedback loop  
3. **Development**  
   - Modular apps: Farm, Marketplace, Blog  
   - RESTful APIs using Django REST Framework  
4. **Testing**  
   - Unit testing using PyTest  
   - UAT with a selected group of farmers  
5. **Deployment**  
   - Gradual rollout to 500+ farms in Phase 1

---


## 📁 Project Structure

```bash
agritracker/
├── agritracker/           # Django settings and routing
├── farm/                  # Farm management app
├── marketplace/           # Produce marketplace app
├── blog/                  # Farmer blog & community sharing
├── templates/             # HTML templates
├── static/                # CSS, JS, and image assets
├── manage.py
├── requirements.txt
└── README.md
```


---

## 🧰 Prerequisites

Make sure you have the following installed on your system:

- ✅ Python 3.8 or higher  
- ✅ pip (Python package manager)  
- ✅ PostgreSQL (recommended) or SQLite (for local development)  
- ✅ Git

---

## 🚀 Local Setup Steps

```bash
# 1. Clone the Repository
git clone https://github.com/your-username/agritracker.git
cd agritracker

# 2. Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Set Up the Database
# This will create the necessary tables
python manage.py makemigrations
python manage.py migrate

# 5. Create a Superuser for Admin Access
python manage.py createsuperuser

# 6. Run the Development Server
python manage.py runserver

```

🖥️ Open in your browser: http://127.0.0.1:8000

