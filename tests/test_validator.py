from src.validator import validate_profile


def test_validator():

    profile = {

        "full_name": "Sample Candidate",

        "emails": [
            "sample.candidate@gmail.com"
        ],

        "phones": [
            "+919876543210"
        ],

        "skills": [
            "Python",
            "Java",
            "Spring Boot"
        ]
    }

    validate_profile(profile)