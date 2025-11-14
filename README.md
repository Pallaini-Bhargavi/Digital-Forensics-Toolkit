# 🔍 Digital Forensics Toolkit

A lightweight Digital Forensics application that detects suspicious files using **entropy analysis** and a **Random Forest machine learning model**.  
It provides a simple GUI to scan files or entire folders and generates a detailed forensic report in CSV format.

---

## ⚙️ Features

- 🧪 **Entropy-based file analysis**  
  Detects abnormal or malicious binary files by examining byte distribution.

- 🤖 **Machine Learning Classification**  
  Uses a trained Random Forest model (`joblib`) to classify files as  
  **Benign** or **Suspicious**.

- 📁 **Scan Single File or Entire Folder**  
  User can choose a file or a directory for analysis.

- 📄 **Automatic Report Generation**  
  Generates a `forensic_report.csv` containing:
  - File name  
  - Suspicious / Not Suspicious status  
  - Serial number  

- 🖥️ **Simple GUI**  
  Clean interface made with Tkinter for easy usage.

---

## 🏗️ Tech Stack

- **Python**
- **Tkinter** (GUI)
- **Scikit-learn** (Random Forest model)
- **Joblib** (model loading)
- **CSV** (report writing)

---

## 📸 Screenshots

### 🧾 Forensic Report Output  
![Report Screenshot](3.jpg)

### 🗂️ Successful Report Generation  
![Success Popup](2.jpg)

### 🖥️ Toolkit Main UI  
![Main UI](1.jpg)

---

## 📂 Project Structure

