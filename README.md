Digital Forensics Toolkit 🔍
A desktop application that detects suspicious files using a trained Random Forest model, based on file size and entropy. It provides an easy-to-use Tkinter GUI and exports results in CSV format.

🚀 Features
-Detect suspicious files using ML
Analyze individual files or entire folders
-Export forensic report (CSV)
-User-friendly GUI (Tkinter)

🛠️ Tech Stack
- Python
- Random Forest (scikit-learn)
- Tkinter
- Pandas, Joblib

📦 Usage
git clone https://github.com/Pallaini-Bhargavi/Digital-Forensics-Toolkit.git
cd Digital-Forensics-Toolkit
python model.py
Ensure random_forest_model.joblib is in the same folder.

📂 Output
Generates forensic_report.csv:
Sl.No, Filename, Suspicious
1, test1.exe, Yes
2, sample.txt, No
