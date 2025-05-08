# PROJECT-FINAL
project 

# Used‑Car Listings Explorer 🚗📊

An interactive Streamlit dashboard for exploring **51 000+** U.S. vehicle‑ad
records.  The app lets you

* **Visualize vehicle‑age distribution** (histogram)  
* **See how many cars were listed per model year** (1980 – 2025)  
* Toggle between the two views with a simple checkbox

> **Tech stack:** Python 3.10 · Streamlit · pandas · plotly.express

---

## Project overview

This project demonstrates how to turn a cleaned CSV dataset into a lightweight
web dashboard.  While it *could* be extended to simulate random
events (e.g., synthetic price generation or demand forecasting), its core
purpose here is **exploratory data analysis** delivered as a one‑click web app.

---

## Directory structure

PROJECT-FINAL/
├── Notebooks
|  ├── .venv 
|  ├──app.py
|  ├──vehicles_us
└── README.md



## How to run locally 🖥️

> Tested on Windows 10 + Python 3.10 / 3.11

```bash
# 1. Clone repo
git clone https://github.com/<your‑user>/<your‑repo>.git
cd <your‑repo>

# 2. Create & activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate           # Windows
# source .venv/bin/activate        # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Streamlit app
streamlit run app.py
Open the printed URL (default: http://localhost:8501) to interact with the
dashboard.