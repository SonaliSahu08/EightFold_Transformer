from src.normalizer import (
    normalize_email,
    normalize_phone,
    normalize_name
)


def test_email():
    assert normalize_email(
        "SAMPLE.CANDIDATE@GMAIL.COM"
    ) == "sample.candidate@gmail.com"


def test_name():
    assert normalize_name(
        "SAMPLE CANDIDATE"
    ) == "Sample Candidate"


def test_phone():
    assert normalize_phone(
        "9876543210"
    ) == "+919876543210"