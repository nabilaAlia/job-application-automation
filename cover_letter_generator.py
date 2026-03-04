def generate_cover_letter(data, company, role, jd_skills):
    name = data.get("name", "")
    degree = data.get("education", [{}])[0].get("degree", "Computer Science graduate")

    skills_line = ", ".join(jd_skills[:8]) if jd_skills else "incident triage, cybersecurity monitoring, and technical documentation"

    return f"""Dear Hiring Manager,

I am writing to apply for the {role} position at {company}. I recently graduated with a background in network engineering and have hands-on internship experience supporting IT operations and cybersecurity work.

During my internship, I supported a Google Workspace to Microsoft 365 migration, helped triage user-reported issues in a ticket-based workflow, and contributed to compliance preparation by gathering evidence for ISO/IEC 27001:2022 and WebTrust CA reviews. I also monitored security alerts using Wazuh SIEM and reviewed logs to support operational integrity.

Based on your job description, I believe my exposure to {skills_line} aligns well with what you are looking for. I enjoy learning quickly, working calmly under pressure, and documenting technical work clearly so teams can move faster.

Thank you for your time and consideration. I would love the opportunity to discuss how I can contribute to your team.

Sincerely,  
{name}
"""
