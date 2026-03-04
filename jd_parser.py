import re

# Start simple: keyword matching (fast + reliable).
SKILL_KEYWORDS = [
    "python", "linux", "wazuh", "siem", "iso", "27001", "webtrust",
    "scap", "cis", "wireshark", "snmp", "tcp/ip", "vlan",
    "microsoft 365", "m365", "google workspace", "migration",
    "incident", "ticket", "troubleshooting", "audit", "compliance",
    "phishing", "gophish"
]

def extract_skills(jd_text: str):
    text = jd_text.lower()
    found = set()

    for skill in SKILL_KEYWORDS:
        pattern = re.escape(skill.lower())
        if re.search(rf"\b{pattern}\b", text):
            found.add(skill)

    return sorted(found)

def detect_role(jd_text: str):
    text = jd_text.lower()
    if "qa" in text or "test" in text or "testing" in text:
        return "QA"
    if "devops" in text or "sre" in text:
        return "DevOps"
    if "security" in text or "soc" in text or "siem" in text:
        return "Cybersecurity"
    if "system administrator" in text or "sysadmin" in text:
        return "System Administrator"
    if "network" in text or "routing" in text:
        return "Network"
    return "General IT"
