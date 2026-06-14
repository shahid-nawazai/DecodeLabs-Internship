# Simple Content-Based Movie Recommendation System

This repository contains a lightweight, command-line Python application that recommends movies based on user interests. By utilizing a **content-based filtering** approach, the system calculates a basic similarity score by matching user-inputted tags against a pre-defined catalog of movies and their genres.

##  Features

* **Dynamic Tag Discovery:** Automatically extracts, aggregates, and displays all unique, sorted tags from the movie database at runtime.
* **Content-Based Scoring:** Tallies a similarity score based on how many user preferences intersect with a movie's features.
* **Ranked Recommendations:** Sorts and displays matching movies in descending order of relevance.
* **Input-Insensitive Matching:** Safely handles varied user inputs by trimming whitespace and normalizing text casing.

---

##  How the Recommendation Engine Works

The core algorithm operates on basic intersection counting:

1. **Tag Processing:** The user inputs interests as a comma-separated string (e.g., `action, sci-fi`). The script splits these into a clean Python list.
2. **Scoring Loop:** For every movie in the catalog, the engine checks how many of the user's preferred tags match the movie's genre tags. Every match increments a `score` counter by `1`.
3. **Sorting:** The results are packed into a list of tuples `(movie_name, score)` and sorted in descending order using:
```python
   recommendations.sort(key=lambda x: x[1], reverse=True)
