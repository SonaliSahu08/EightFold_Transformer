import requests


def fetch_github_profile(username):
    """
    Fetch public GitHub profile information.
    """

    if not username:
        return {}

    url = f"https://api.github.com/users/{username}"

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={
                "Accept": "application/vnd.github+json"
            }
        )

        if response.status_code != 200:
            print("GitHub profile not found.")
            return {}

        data = response.json()

        return {

            "username": data.get("login"),

            "name": data.get("name"),

            "followers": data.get("followers"),

            "following": data.get("following"),

            "public_repos": data.get("public_repos"),

            "company": data.get("company"),

            "location": data.get("location"),

            "blog": data.get("blog"),

            "profile_url": data.get("html_url")

        }

    except requests.RequestException as e:

        print(f"GitHub API Error: {e}")

        return {}