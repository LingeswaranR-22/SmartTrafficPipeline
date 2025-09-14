# 🚦 SmartTrafficPipeline

A fully automated ETL pipeline for processing and analyzing Dubai traffic incident data. Built with modular components, cloud integration, and professional-grade alerts.

---

## 🔧 Features

- ✅ Extracts raw traffic data from CSV
- ✅ Cleans and transforms into structured format
- ✅ Generates summary reports and top-location charts
- ✅ Uploads files to Google Drive (OAuth-based)
- ✅ Sends email alerts via Gmail (App Password)

---

## 📁 Folder Structure

SmartTrafficPipeline/ 
├── config/             # Email and path settings 
├── data/               # Raw and processed traffic data 
├── etl/                # Modular ETL components
├── logs/               # Pipeline logs 
├── pipeline.py         # Main runner script 
├── README.md           # Project overview 
├── requirements.txt    # Python dependencies 
└── .gitignore          # Files to exclude from Git

---

## ▶️ How to Run

1. **Add credentials**
   - Place `client_secrets.json` in the root folder
   - Configure `config/config.py` with your Gmail App Password

2. **Activate virtual environment**
   ```bash
   .\.venv\Scripts\Activate.ps1

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   Run the pipeline

4. **Run the Pipeline**
   ```bash
   python pipeline.py

## 📊 Sample Output

summary_YYYYMMDD_HHMMSS.csv: Incident summary

top_locations.png: Bar chart of top 5 locations

traffic_clean.csv: Cleaned dataset

traffic_clean.zip: Archived version

- All files are uploaded to Google Drive under:
   ```bash
   SmartTrafficPipeline/YYYY-MM-DD/

## 📦 Dependencies

PyDrive

matplotlib

requests

smtplib (built-in)

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 👤 Author
Lingeswaran R

Data Engineer