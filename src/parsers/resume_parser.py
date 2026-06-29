import pdfplumber


def parse_resume(path):
    """
    Extract raw text from resume PDF.
    """

    text = ""

    with pdfplumber.open(path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return [{
        "source": "Resume PDF",
        "raw_text": text
    }]