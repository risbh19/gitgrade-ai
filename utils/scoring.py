def calculate_score(data: dict):
    """
    Rule-based scoring system (0–100)
    """
    score = 0
    reasons = []

    # Project size
    if data["file_count"] >= 15:
        score += 20
        reasons.append("Good project size")
    elif data["file_count"] >= 5:
        score += 10
        reasons.append("Moderate project size")
    else:
        reasons.append("Very small project")

    # README
    if data["has_readme"]:
        score += 20
        reasons.append("README present")
    else:
        reasons.append("Missing README")

    # Tests
    if data["has_tests"]:
        score += 20
        reasons.append("Tests detected")
    else:
        reasons.append("No tests found")

    # Commits
    if data["commit_count"] >= 20:
        score += 20
        reasons.append("Consistent commit history")
    elif data["commit_count"] >= 5:
        score += 10
        reasons.append("Some commit history")
    else:
        reasons.append("Poor commit history")

    # Tech stack
    if data["language"]:
        score += 20
        reasons.append("Clear primary language")

    return min(score, 100), reasons
