import requests

URL = "https://api.github.com/users/nayyen"


def get_profile(url: str) -> dict:
    """Fetch a GitHub profile and return it as a dict."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # raise an error for 4xx/5xx responses
    return response.json()


def main() -> None:
    try:
        data = get_profile(URL)
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return

    print(f"Name      : {data['name']}")
    print(f"Username  : {data['login']}")
    print(f"Repos     : {data['public_repos']}")
    print(f"Followers : {data['followers']}")


if __name__ == "__main__":
    main()