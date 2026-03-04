import csv
from datetime import date
from pathlib import Path

def log_application(company, role, resume_path, cover_letter_path):
    Path("output").mkdir(exist_ok=True)
    file_path = Path("output/applications.csv")

    is_new = not file_path.exists()

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["date", "company", "role", "resume_file", "cover_letter_file", "status"])
        writer.writerow([str(date.today()), company, role, resume_path, cover_letter_path, "Applied"])
