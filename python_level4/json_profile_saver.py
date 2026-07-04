import json
profile = {"name": "Monii","skills": ["Python", "SQL", "AI"],"level": "Beginner"}
with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)
with open("profile.json", "r") as file:
    data = json.load(file)
print("Name:", data["name"])
print("Skills:", ", ".join(data["skills"]))
print("Level:", data["level"])