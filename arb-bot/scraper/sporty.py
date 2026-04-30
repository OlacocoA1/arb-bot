import requests

def get_sporty():
    try:
        url = "https://www.sportybet.com/ng/m/"

        r = requests.get(url, timeout=10)
        data = r.json()

        # expected format after mapping
        return {
            "Team A vs Team B": 2.10,
            "Team C vs Team D": 1.95
        }

    except:
        return {}
