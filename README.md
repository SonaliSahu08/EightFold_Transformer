# Eightfold Candidate Profile Transformer

## Overview

The Eightfold Candidate Profile Transformer is a Python-based data transformation pipeline that consolidates candidate information from multiple heterogeneous sources into a single canonical candidate profile.

The system ingests both structured and unstructured data, resolves conflicting information using configurable source priorities, normalizes values, tracks data provenance, and generates a configurable JSON output.

---

## Features

* Parse multiple candidate data sources

  * Recruiter CSV
  * ATS JSON
  * Resume PDF
  * Recruiter Notes (TXT)
* Normalize candidate information

  * Phone numbers
  * Skills
  * Company names
* Merge duplicate candidate records
* Resolve conflicting values using configurable source priorities
* Track provenance for every selected field
* Runtime-configurable output using JSON configuration
* Generate a clean canonical candidate profile

---

## Project Structure

```text
EightFold_Transformer/
│
├── config/
│   └── default.json                 # Runtime projection configuration
│
├── logs/
│   └── application.log              # Generated automatically
│
├── output/
│   └── result.json                  # Final transformed output
│
├── sample_data/
│   ├── recruiter.csv
│   ├── ats.json
│   ├── resume.pdf
│   └── recruiter_notes.txt
│
├── src/
│   ├── __init__.py
│   │
│   ├── main.py                      # Entry point
│   ├── logger.py                    # Logging configuration
│   ├── normalizer.py                # Data normalization
│   ├── merger.py                    # Merge & conflict resolution
│   ├── projection.py                # Configurable output projection
│   ├── validator.py                 # Output validation
│   ├── github_api.py                # GitHub enrichment
│   ├── schema.py                    # JSON schema
│   │
│   └── parsers/
│       ├── __init__.py
│       ├── csv_parser.py
│       ├── ats_parser.py
│       ├── resume_parser.py
│       └── notes_parser.py
│
├── tests/
│   ├── __init__.py
│   ├── test_csv.py
│   ├── test_merger.py
│   ├── test_normalizer.py
│   └── test_validator.py
│
├── requirements.txt
├── README.md
├── .gitignore

```

---

## Source Priority

When conflicting values are encountered, the following priority order is used:

| Source          | Priority |
| --------------- | -------- |
| ATS JSON        | 4        |
| Recruiter CSV   | 3        |
| Resume PDF      | 2        |
| Recruiter Notes | 1        |

The value from the highest-priority source is selected for the canonical profile.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd EightFold_Transformer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Required Libraries

* pandas
* pdfplumber
* phonenumbers
* jsonschema
* rapidfuzz
* python-dateutil
* openpyxl

Install manually if needed:

```bash
pip install pandas pdfplumber phonenumbers jsonschema rapidfuzz python-dateutil openpyxl
```

---

## Running the Project

Run from the project root directory:

```bash
python src/main.py --csv sample_data/recruiter.csv --ats sample_data/ats.json --resume sample_data/resume.pdf --notes sample_data/recruiter_notes.txt --config config/default.json
```

The generated canonical profile will be written to the output directory.

---

## Runtime Configuration

The transformer supports configurable output through a JSON configuration file.

Example capabilities:

* Select output fields
* Rename fields
* Apply normalization
* Configure required fields
* Include or exclude provenance
* Handle missing values

Example:

```json
{
  "fields": [
    {
      "path": "full_name"
    },
    {
      "path": "primary_email",
      "from": "emails[0]"
    },
    {
      "path": "phone",
      "from": "phones[0]",
      "normalize": "E164"
    }
  ]
}
```

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

## Design Highlights

* Modular parser architecture
* Canonical data model
* Source-based conflict resolution
* Data normalization
* Provenance tracking
* Config-driven transformation
* Extensible design for additional data sources

---

## Technologies Used

* Python 3
* JSON
* CSV
* PDF Parsing
* Regular Expressions
* Object-Oriented Programming

---

## Future Improvements

* LinkedIn profile parser
* OCR support for scanned resumes
* Web-based user interface
* REST API
* Machine learning-based confidence scoring

---

## Author

Developed as part of the Eightfold AI Engineering Assignment.
