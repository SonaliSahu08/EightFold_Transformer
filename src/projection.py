import json
import os


def project_output(profile, config_path=None):
    """
    Projects the merged profile according to a JSON configuration.
    """

    # No configuration supplied
    if not config_path:
        return profile

    if not os.path.exists(config_path):
        print("Configuration file not found.")
        return profile

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    projected = {}

    fields = config.get("fields", [])

    for field in fields:

        output_name = field.get("output")

        profile_key = field.get("path")

        projected[output_name] = profile.get(profile_key)

    return projected