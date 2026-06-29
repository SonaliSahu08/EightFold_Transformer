import json


def parse_ats(path):
    """
    Parse ATS JSON.
    """

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict):
        data = [data]

    records = []

    for candidate in data:

        records.append({
            "source": "ATS JSON",
            "name": candidate.get("candidateName"),
            "email": candidate.get("mail"),
            "phone": candidate.get("mobile"),
            "company": candidate.get("organization"),
            "title": candidate.get("designation")
        })

    return records