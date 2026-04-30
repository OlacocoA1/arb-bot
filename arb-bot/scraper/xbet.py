import requests

def get_xbet():
    try:
        url = "https://example-xbet-endpoint.com"

        r = requests.get(url, timeout=10)
        data = r.json()

        return {
            "Team A vs Team B": 2.05,
            "Team C vs Team D": 2.00
        }

    except:
        return {}
