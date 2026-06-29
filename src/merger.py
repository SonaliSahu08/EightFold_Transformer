from collections import defaultdict

# Higher value = higher trust
SOURCE_PRIORITY = {
    "ATS JSON": 4,
    "Recruiter CSV": 3,
    "Resume PDF": 2,
    "Recruiter Notes": 1
}


def merge_records(records):
    """
    Merge normalized records into one canonical candidate profile.

    Returns:
        dict
    """

    if not records:
        raise ValueError("No records available to merge.")

    merged = defaultdict(lambda: None)

    emails = []
    phones = []
    skills = []

    provenance = {}
    confidence = {}
    field_priority = {}

    def update_field(output_field, input_field):
        """
        Update a single-value field using source priority.
        """

        for record in records:

            value = record.get(input_field)

            if not value:
                continue

            source = record.get("source", "Unknown")

            priority = SOURCE_PRIORITY.get(source, 0)

            if (
                merged[output_field] is None
                or priority > field_priority.get(output_field, -1)
            ):

                merged[output_field] = value

                field_priority[output_field] = priority

                provenance[output_field] = source

                confidence[output_field] = round(priority / 4, 2)

    # -----------------------------
    # Merge single-value fields
    # -----------------------------

    update_field("full_name", "name")
    update_field("current_company", "company")
    update_field("current_title", "title")
    update_field("github_username", "github")

    # -----------------------------
    # Merge list fields
    # -----------------------------

    email_sources = {}
    phone_sources = {}
    skill_sources = {}

    for record in records:

        source = record.get("source", "Unknown")

        # Emails
        email = record.get("email")

        if email and email not in emails:
            emails.append(email)
            email_sources[email] = source

        # Phones
        phone = record.get("phone")

        if phone and phone not in phones:
            phones.append(phone)
            phone_sources[phone] = source

        # Skills
        for skill in record.get("skills", []):

            if skill not in skills:
                skills.append(skill)
                skill_sources[skill] = source

    merged["emails"] = emails
    merged["phones"] = phones
    merged["skills"] = skills

    provenance["emails"] = email_sources
    provenance["phones"] = phone_sources
    provenance["skills"] = skill_sources

    confidence["emails"] = 1.0 if emails else 0.0
    confidence["phones"] = 1.0 if phones else 0.0
    confidence["skills"] = 1.0 if skills else 0.0

    merged["provenance"] = provenance
    merged["confidence"] = confidence

    return dict(merged)