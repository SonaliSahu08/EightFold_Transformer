# Eightfold Candidate Profile Transformer

A Python-based data transformation pipeline that consolidates candidate information from multiple structured and unstructured sources into a single canonical candidate profile.

The transformer normalizes data, resolves conflicting values using source priorities, tracks provenance, validates the output, and produces a configurable JSON profile.

---

## Features

- Parse multiple candidate data sources:
  - Recruiter CSV
  - ATS JSON
  - Resume PDF
  - Recruiter Notes (TXT)
- Normalize candidate information (phone numbers, skills, company names)
- Merge duplicate records using configurable source priorities
- Track provenance for every selected field
- Validate the final profile using a JSON schema
- Support configurable output projection through a runtime configuration file

---

## Pipeline

```text
Input Sources
      │
      ▼
    Parsers
      │
      ▼
 Normalization
      │
      ▼
 Merge & Conflict Resolution
      │
      ▼
 Provenance Tracking
      │
      ▼
 Validation
      │
      ▼
 Configurable Projection
      │
      ▼
 Canonical JSON Output
```

---

## Project Structure

```text
EightFold_Transformer/
│
├── config/
├── sample_data/
├── src/
│   ├── parsers/
│   ├── main.py
│   ├── merger.py
│   ├── normalizer.py
│   ├── projection.py
│   ├── validator.py
│   ├── schema.py
│   ├── github_api.py
│   └── logger.py
│
├── tests/
├── output/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Conflict Resolution

When multiple sources contain different values for the same field, the transformer selects the value based on the following priority:

1. ATS JSON
2. Recruiter CSV
3. Resume PDF
4. Recruiter Notes

All selected values retain provenance information indicating their source.

---

## Installation

Clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd EightFold_Transformer
pip install -r requirements.txt
```

---

## Running the Project

Run the transformer from the project root directory:

```bash
python src/main.py --csv sample_data/recruiter.csv --ats sample_data/ats.json --resume sample_data/resume.pdf --notes sample_data/recruiter_notes.txt --config config/default.json
```

The transformed candidate profile is generated in the `output/` directory.

---

## Sample Output

```json
{
  "full_name": "Sample Candidate",
  "primary_email": "sample.candidate@example.com",
  "phone": "+919876543210",
  "current_company": "TechNova Solutions",
  "current_title": "Software Engineer",
  "skills": [
    "Java",
    "Python",
    "Spring Boot",
    "SQL"
  ],
  "provenance": {
    "full_name": "ATS JSON",
    "current_company": "Recruiter CSV",
    "skills": "Resume PDF"
  }
}
```

---

## Technologies Used

- Python 3
- Pandas
- PDFPlumber
- JSON Schema
- Phonenumbers
- RapidFuzz
- Python-Dateutil

---

## Testing

Run the test suite using:

```bash
pytest -v
```

Current status:

```
6 tests passed
```

---

## Future Improvements

- LinkedIn profile integration
- OCR support for scanned resumes
- REST API interface
- Web-based dashboard
- Machine learning-based confidence scoring

---

## Author

**Sonali Sahu**

Developed for the **Eightfold Engineering Intern Assignment**.
