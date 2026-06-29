import re
from jsonschema import validate

try:
    from .schema import PROFILE_SCHEMA
except ImportError:
    from schema import PROFILE_SCHEMA


EMAIL_PATTERN = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

PHONE_PATTERN = r'^\+[1-9]\d{7,14}$'


def validate_profile(profile):
    """
    Validate final merged profile.
    """

    # JSON Schema validation
    validate(
        instance=profile,
        schema=PROFILE_SCHEMA
    )

    # Validate email list
    for email in profile.get("emails", []):

        if not re.match(EMAIL_PATTERN, email):

            raise ValueError(
                f"Invalid email: {email}"
            )

    # Validate phone list
    for phone in profile.get("phones", []):

        if not re.match(PHONE_PATTERN, phone):

            raise ValueError(
                f"Invalid phone number: {phone}"
            )

    print("Profile validation successful.")