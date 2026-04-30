def normalize_team(name):
    """
    Standardizes team names so both bookmakers match correctly.
    """

    name = name.lower().strip()

    replacements = {
        "man utd": "manchester united",
        "man united": "manchester united",
        "barca": "barcelona",
        "psg": "paris saint germain",
        "inter milan": "inter",
        "real madrid cf": "real madrid",
        "bayern munich": "bayern"
    }

    return replacements.get(name, name)
  def normalize_match(match):
    """
    Converts full match string into comparable format
    """

    teams = match.lower().split(" vs ")

    if len(teams) != 2:
        return match.lower()

    team1 = normalize_team(teams[0])
    team2 = normalize_team(teams[1])

    return f"{team1} vs {team2}"
