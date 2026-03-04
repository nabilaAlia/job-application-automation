import json
import os

from src.jd_parser import extract_skills, detect_role
from src.skill_matcher import select_experience_blocks
from src.resume_generator import generate_resume_docx
from src.cover_letter_generator import generate_cover_letter
from src.tracker import log_application

def read_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)

def safe_filename(text):
    return "".join(c if c.isalnum() or c in ("_", "-") else "_" for c in text).strip("_")

def main():
    print("\n=== Job Application Automation (CLI) ===\n")

    company = input("Company name: ").strip()
    role_input = input("Target role (e.g. Cybersecurity / Network / IT): ").strip()

    jd_text = read_multiline_input("\nPaste Job Description (press ENTER twice to finish):")

    with open("data/master_resume.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    jd_skills = extract_skills(jd_text)
    role_detected = detect_role(jd_text)

    selected_experience = select_experience_blocks(data["experience"], jd_skills)

    os.makedirs("output/resumes", exist_ok=True)
    os.makedirs("output/cover_letters", exist_ok=True)

    company_fn = safe_filename(company)
    role_fn = safe_filename(role_input)

    resume_path = f"output/resumes/{company_fn}_{role_fn}.docx"
    cover_letter_path = f"output/cover_letters/{company_fn}_{role_fn}.txt"

    # Generate resume
    generate_resume_docx(data, selected_experience, jd_skills, company, role_input, resume_path)

    # Generate cover letter
    cover_letter = generate_cover_letter(data, company, role_input, jd_skills)
    with open(cover_letter_path, "w", encoding="utf-8") as f:
        f.write(cover_letter)

    # Log application
    log_application(company, role_input, resume_path, cover_letter_path)

    print("\n--- JD Analysis ---")
    print("Detected role:", role_detected)
    print("Matched skills:", ", ".join(jd_skills) if jd_skills else "(none found yet)")

    print("\n✅ Generated:")
    print("📄 Resume:", resume_path)
    print("✉️ Cover letter:", cover_letter_path)
    print("📌 Tracker: output/applications.csv\n")

if __name__ == "__main__":
    main()
