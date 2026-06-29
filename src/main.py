import argparse
import json
import os

from parsers.csv_parser import parse_csv
from parsers.ats_parser import parse_ats
from parsers.resume_parser import parse_resume
from parsers.notes_parser import parse_notes

from normalizer import normalize_record
from merger import merge_records
from validator import validate_profile
from projection import project_output
from github_api import fetch_github_profile

from logger import setup_logger


logger = setup_logger()


def parse_sources(args):
    """
    Parse all available input sources.
    """

    records = []

    if args.csv:
        logger.info("Reading Recruiter CSV...")
        records.extend(parse_csv(args.csv))

    if args.ats:
        logger.info("Reading ATS JSON...")
        records.extend(parse_ats(args.ats))

    if args.resume:
        logger.info("Reading Resume PDF...")
        records.extend(parse_resume(args.resume))

    if args.notes:
        logger.info("Reading Recruiter Notes...")
        records.extend(parse_notes(args.notes))

    return records


def main():

    parser = argparse.ArgumentParser(
        description="Eightfold Multi-Source Candidate Data Transformer"
    )

    parser.add_argument(
        "--csv",
        help="Path to Recruiter CSV"
    )

    parser.add_argument(
        "--ats",
        help="Path to ATS JSON"
    )

    parser.add_argument(
        "--resume",
        help="Path to Resume PDF"
    )

    parser.add_argument(
        "--notes",
        help="Path to Recruiter Notes"
    )

    parser.add_argument(
        "--config",
        help="Projection Configuration JSON"
    )

    args = parser.parse_args()

    print("=" * 70)
    print(" Eightfold Multi-Source Candidate Data Transformer ")
    print("=" * 70)

    try:

        # ---------------------------------------------------
        # Step 1 : Parse Input Sources
        # ---------------------------------------------------

        raw_records = parse_sources(args)

        logger.info(f"Parsed {len(raw_records)} record(s).")

        # ---------------------------------------------------
        # Step 2 : Normalize
        # ---------------------------------------------------

        normalized_records = []

        for record in raw_records:

            normalized_records.append(
                normalize_record(record)
            )

        logger.info("Normalization completed.")

        # ---------------------------------------------------
        # Step 3 : Merge
        # ---------------------------------------------------

        merged_profile = merge_records(
            normalized_records
        )

        logger.info("Merge completed.")

        # ---------------------------------------------------
        # Step 4 : GitHub Enrichment
        # ---------------------------------------------------

        github_username = merged_profile.get(
            "github_username"
        )

        if github_username:

            logger.info(
                f"Fetching GitHub profile for {github_username}"
            )

            merged_profile["github_profile"] = (
                fetch_github_profile(
                    github_username
                )
            )

        # ---------------------------------------------------
        # Step 5 : Validation
        # ---------------------------------------------------

        validate_profile(
            merged_profile
        )

        logger.info(
            "Validation successful."
        )

        # ---------------------------------------------------
        # Step 6 : Projection
        # ---------------------------------------------------

        final_output = project_output(
            merged_profile,
            args.config
        )

        # ---------------------------------------------------
        # Step 7 : Save Output
        # ---------------------------------------------------

        os.makedirs(
            "output",
            exist_ok=True
        )

        output_path = os.path.join(
            "output",
            "result.json"
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                final_output,
                file,
                indent=4,
                ensure_ascii=False
            )

        logger.info(
            f"Output saved to {output_path}"
        )

        print("\nTransformation Completed Successfully.\n")

        print(json.dumps(
            final_output,
            indent=4,
            ensure_ascii=False
        ))

    except Exception as e:

        logger.exception("Pipeline execution failed.")

        print("\nPipeline Failed!")

        print(e)


if __name__ == "__main__":
    main()