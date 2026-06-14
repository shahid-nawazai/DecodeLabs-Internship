items = {
    "The Matrix": ["action","sci-fi", "technology"],
    "Interstellar": ["sci-fi", "space", "adventure"],
    "Avengers": ["action", "superhero", "adventure"],
    "Titanic": ["romance", "drama"],
    "Inception": ["action", "sci-fi", "thriller"],
    "The Notebook": ["romance", "drama"],
    "John Wick": ["action", "thriller"],
    "Coco": ["animation", "family", "music"]
}

print("===== AI Recommendation System =====")
print("\nAvailable Interests:")
all_tags = set()

for tags in items.values():
    all_tags.update(tags)

print(", ".join(sorted(all_tags)))

user_input = input("\nEnter your interests (comma separated): ").lower()
user_preferences = [x.strip() for x in user_input.split(",")]

recommendations = []

for item, features in items.items():
    score = 0

    for pref in user_preferences:
        if pref in features:
            score += 1

    recommendations.append((item, score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\n===== Recommended Items =====")

found = False

for item, score in recommendations:
    if score > 0:
        print(f"{item}  | Similarity Score: {score}")
        found = True

if not found:
    print("No matching recommendations found.")