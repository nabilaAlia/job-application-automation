def score_bullet(bullet_tags, jd_skills):
    # Normalize to lowercase for matching
    tags = {t.lower() for t in bullet_tags}
    skills = {s.lower() for s in jd_skills}
    return len(tags.intersection(skills))

def select_best_bullets(experience, jd_skills, max_bullets=5):
    # Flatten bullets and score them
    bullets = []
    for exp in experience:
        for b in exp.get("bullets", []):
            bullets.append((b, score_bullet(b.get("tags", []), jd_skills)))

    # Sort: highest score first, keep top N
    bullets.sort(key=lambda x: x[1], reverse=True)
    selected = [b for (b, score) in bullets if score > 0][:max_bullets]

    return selected

def select_experience_blocks(experience, jd_skills):
    # Keep experiences that have at least 1 matching bullet
    selected_blocks = []
    for exp in experience:
        matching = []
        for b in exp.get("bullets", []):
            if score_bullet(b.get("tags", []), jd_skills) > 0:
                matching.append(b)
        if matching:
            # Replace bullets with only matching bullets (top 5)
            matching.sort(key=lambda b: score_bullet(b.get("tags", []), jd_skills), reverse=True)
            exp_copy = dict(exp)
            exp_copy["bullets"] = matching[:5]
            selected_blocks.append(exp_copy)

    # If nothing matches, return everything (fallback)
    return selected_blocks if selected_blocks else experience
