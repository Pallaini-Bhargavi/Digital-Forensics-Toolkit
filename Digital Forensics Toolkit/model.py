import os
import math
import tkinter as tk
from tkinter import filedialog, messagebox
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the trained model
model = joblib.load("random_forest_model.joblib")

# Function to calculate entropy of a file
def calculate_entropy(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            if not data:
                return 0
            byte_freq = [0] * 256
            for byte in data:
                byte_freq[byte] += 1
            entropy = 0
            for freq in byte_freq:
                if freq > 0:
                    p = freq / len(data)
                    entropy -= p * math.log2(p)
            return entropy
    except Exception:
        return 0

# Function to extract features from a file
def extract_features(file_path):
    try:
        size = os.path.getsize(file_path)
        entropy = calculate_entropy(file_path)
        return {
            "size": size,
            "entropy": entropy
        }
    except Exception:
        return {
            "size": 0,
            "entropy": 0
        }

# Save results to CSV with spacing
def save_report(results, save_folder):
    report_path = os.path.join(save_folder, "forensic_report.csv")
    with open(report_path, "w", newline='') as f:
        f.write(f"{'Sl.No':<10},{'Filename':<30},{'Suspicious':<15}\n")
        for i, (filename, pred) in enumerate(results, start=1):
            suspicious_text = "Yes" if pred == 1 else "No"
            f.write(f"{str(i):<10},{os.path.basename(filename):<30},{suspicious_text:<15}\n")

# Handle single file input
def handle_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        features = extract_features(file_path)
        prediction = model.predict(pd.DataFrame([features]))[0]
        results = [(file_path, prediction)]
        save_report(results, os.path.dirname(file_path))
        messagebox.showinfo("Success", "Report saved successfully to forensic_report.csv")

# Handle folder input
def handle_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        results = []
        for filename in os.listdir(folder_path):
            full_path = os.path.join(folder_path, filename)
            if os.path.isfile(full_path):
                features = extract_features(full_path)
                prediction = model.predict(pd.DataFrame([features]))[0]
                results.append((full_path, prediction))
        save_report(results, folder_path)
        messagebox.showinfo("Success", "Report saved successfully to forensic_report.csv")

# GUI setup
root = tk.Tk()
root.title("Digital Forensics Toolkit")
root.geometry("400x200")

btn_file = tk.Button(root, text="Select File", command=handle_file, width=30)
btn_file.pack(pady=20)

btn_folder = tk.Button(root, text="Select Folder", command=handle_folder, width=30)
btn_folder.pack(pady=10)

root.mainloop()
