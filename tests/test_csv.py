import tempfile
import pandas as pd

from src.parsers.csv_parser import parse_csv
def test_csv_parser():

    df = pd.DataFrame({

        "name": [
            "Sample Candidate"
        ], 

        "email": [
            "sample.candidate@gmail.com"
        ],

        "phone": [
            "9876543210"
        ],

        "current_company": [
            "Google"
        ],

        "title": [
            "Software Engineer"
        ]

    })

    with tempfile.NamedTemporaryFile(
        suffix=".csv",
        delete=False
    ) as temp:

        df.to_csv(
            temp.name,
            index=False
        )

        result = parse_csv(temp.name)

    assert result[0]["name"] == "Sample Candidate"

    assert result[0]["email"] == "sample.candidate@gmail.com"

    assert result[0]["company"] == "Google"

    assert result[0]["title"] == "Software Engineer"