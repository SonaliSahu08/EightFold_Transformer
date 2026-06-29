def parse_notes(path):
    """
    Read recruiter notes.
    """

    with open(path, "r", encoding="utf-8") as file:

        text = file.read()

    return [{
        "source": "Recruiter Notes",
        "raw_text": text
    }]