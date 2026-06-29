import re
import phonenumbers
from dateutil import parser as date_parser


def normalize_name(name):
    """
    Convert names to title case.
    """
    if not name:
        return None

    return " ".join(name.strip().title().split())


def normalize_email(email):
    """
    Lowercase email and remove spaces.
    """
    if not email:
        return None

    return email.strip().lower()


def normalize_phone(phone):
    """
    Convert phone number to E.164 format.
    """

    if not phone:
        return None

    try:

        phone = str(phone)

        if not phone.startswith("+"):
            phone = "+91" + phone.strip()

        parsed = phonenumbers.parse(phone)

        return phonenumbers.format_number(
            parsed,
            phonenumbers.PhoneNumberFormat.E164
        )

    except:
        return phone


def normalize_company(company):

    if not company:
        return None

    return company.strip().title()


def normalize_title(title):

    if not title:
        return None

    return title.strip().title()


def extract_skills(text):
    """
    Very simple keyword extraction.
    We'll improve this later.
    """

    if not text:
        return []

    skills = [
        "Python",
        "Java",
        "Spring Boot",
        "React",
        "SQL",
        "AWS",
        "Docker",
        "Git",
        "C++",
        "JavaScript"
    ]

    found = []

    lower_text = text.lower()

    for skill in skills:

        if skill.lower() in lower_text:
            found.append(skill)

    return found


def normalize_record(record):
    """
    Normalize every parsed record.
    """

    normalized = {}

    normalized["source"] = record.get("source")

    normalized["name"] = normalize_name(
        record.get("name")
    )

    normalized["email"] = normalize_email(
        record.get("email")
    )

    normalized["phone"] = normalize_phone(
        record.get("phone")
    )

    normalized["company"] = normalize_company(
        record.get("company")
    )

    normalized["title"] = normalize_title(
        record.get("title")
    )
    normalized["github"] = normalize_github(
    record.get("github")
)

    raw_text = record.get("raw_text", "")

    normalized["skills"] = extract_skills(raw_text)

    normalized["raw_text"] = raw_text

    return normalized
def normalize_github(username):

    if not username:
        return None

    return username.strip()