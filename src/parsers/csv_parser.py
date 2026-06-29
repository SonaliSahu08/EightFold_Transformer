import pandas as pd


def parse_csv(path):
    """
    Parse recruiter CSV file.

    Returns:
        List[dict]
    """

    df = pd.read_csv(path)

    records = []

    for _, row in df.iterrows():

        records.append({
            "source": "Recruiter CSV",
            "name": row.get("name"),
            "email": row.get("email"),
            "phone": row.get("phone"),
            "company": row.get("current_company"),
            "title": row.get("title")
        })

    return records