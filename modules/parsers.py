def parse(feet_inches):
    parts = feet_inches.split(" ")
    return {"feet": int(parts[0]), "inches": float(parts[1])}
