from src.merger import merge_records


def test_merge():

    records = [

        {
            "source": "ATS JSON",
            "name": "Sample Candidate",
            "email": "sample.candidate@gmail.com",
            "phone": "+919876543210",
            "company": "Google",
            "title": "Software Engineer",
            "skills": ["Python"]
        },

        {
            "source": "Resume PDF",
            "skills": [
                "Java",
                "Spring Boot"
            ]
        }

    ]

    merged = merge_records(records)

    assert merged["full_name"] == "Sample Candidate"

    assert "Python" in merged["skills"]

    assert "Java" in merged["skills"]

    assert "Spring Boot" in merged["skills"]

    assert len(merged["skills"]) == 3