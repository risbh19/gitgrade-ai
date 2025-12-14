def generate_summary(data, score):
    return (
        f"The repository demonstrates a {data['language']} based project with "
        f"{data['file_count']} files and a total score of {score}/100. "
        "The evaluation highlights current strengths while identifying clear areas for improvement."
    )

def generate_roadmap(data):
    roadmap = []

    if not data["has_readme"]:
        roadmap.append("Add a comprehensive README with setup instructions and project overview")

    if not data["has_tests"]:
        roadmap.append("Introduce unit tests to improve reliability and maintainability")

    if data["commit_count"] < 10:
        roadmap.append("Commit code more frequently with meaningful messages")

    roadmap.extend([
        "Refactor code for better readability and modularity",
        "Add CI/CD using GitHub Actions"
    ])

    return roadmap
