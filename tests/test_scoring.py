from utils.scoring import calculate_score

def test_high_quality_repo():
    data = {
        "file_count": 20,
        "has_readme": True,
        "has_tests": True,
        "commit_count": 30,
        "language": "Python"
    }
    score, _ = calculate_score(data)
    assert score >= 80

def test_low_quality_repo():
    data = {
        "file_count": 2,
        "has_readme": False,
        "has_tests": False,
        "commit_count": 1,
        "language": None
    }
    score, _ = calculate_score(data)
    assert score <= 30
