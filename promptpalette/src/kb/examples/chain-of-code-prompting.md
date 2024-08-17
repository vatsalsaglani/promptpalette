---
Paper: Chain of Code - Reasoning with a Language Model-Augmented Code Emulator
Link: https://arxiv.org/abs/2312.04474v4
---

Here's a prompt with examples for Chain of Code (CoC) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of solving problems by generating and executing code. When presented with a task, write Python code to solve it, then execute each line, using an emulator when necessary. Here's an example:

user: `What holiday is 314 days after Valentine's Day in 2024?`

assistant: To solve this problem, I'll generate and execute Python code:

```python
1 from datetime import date, timedelta
2 valentines_day = date(2024, 2, 14)
3 target_date = valentines_day + timedelta(days=314)
4 def get_holiday(date):
    # Emulator: This function would check a holiday database
    if date.month == 12 and date.day == 24:
        return "Christmas Eve"
    return "No major holiday"
5 holiday = get_holiday(target_date)
6 print(f"The date is {target_date}, which is {holiday}")
```

Execution:
Line 1: Imported necessary modules
Line 2: valentines_day = date(2024, 2, 14)
Line 3: target_date = date(2024, 12, 24)
Line 4: Defined get_holiday function (emulated)
Line 5: holiday = "Christmas Eve"
Line 6: Output: The date is 2024-12-24, which is Christmas Eve

The holiday 314 days after Valentine's Day in 2024 is Christmas Eve.

user: ``Find a movie similar to Batman, The Mask, The Fugitive, Pretty Woman from these options: (A) The Front Page, (B) Maelstrom, (C) The Lion King, (D) Lamerica``

assistant: To solve this problem, I'll generate and execute Python code:

```python
1 def get_movie_genre_and_year(movies):
    # Emulator: This function would fetch movie data from a database
    movie_data = {
        "Batman": ("action", 1989),
        "The Mask": ("comedy", 1994),
        "The Fugitive": ("thriller", 1993),
        "Pretty Woman": ("romance", 1990),
        "The Front Page": ("comedy", 1974),
        "Maelstrom": ("drama", 2000),
        "The Lion King": ("animation", 1994),
        "Lamerica": ("drama", 1994)
    }
    return [movie_data[movie] for movie in movies if movie in movie_data]

2 def get_most_similar_movie(query_movies, ref_movies, ref_movie_infos):
    # Emulator: This function would use a similarity algorithm
    # For simplicity, we'll just count genre matches
    genre_counts = {}
    for movie, (genre, _) in zip(query_movies, get_movie_genre_and_year(query_movies)):
        matches = sum(1 for ref_genre, _ in ref_movie_infos if ref_genre == genre)
        genre_counts[movie] = matches
    return max(genre_counts, key=genre_counts.get)

3 options = {"A": "The Front Page", "B": "Maelstrom", "C": "The Lion King", "D": "Lamerica"}
4 query_movies = list(options.values())
5 ref_movies = ["Batman", "The Mask", "The Fugitive", "Pretty Woman"]
6 ref_movie_infos = get_movie_genre_and_year(ref_movies)
7 most_similar = get_most_similar_movie(query_movies, ref_movies, ref_movie_infos)
8 answer = next(key for key, value in options.items() if value == most_similar)
9 print(f"The most similar movie is option ({answer}): {most_similar}")
```

Execution:
Lines 1-2: Defined helper functions (emulated)
Line 3: options = {"A": "The Front Page", "B": "Maelstrom", "C": "The Lion King", "D": "Lamerica"}
Line 4: query_movies = ["The Front Page", "Maelstrom", "The Lion King", "Lamerica"]
Line 5: ref_movies = ["Batman", "The Mask", "The Fugitive", "Pretty Woman"]
Line 6: ref_movie_infos = [("action", 1989), ("comedy", 1994), ("thriller", 1993), ("romance", 1990)]
Line 7: most_similar = "The Lion King"
Line 8: answer = "C"
Line 9: Output: The most similar movie is option (C): The Lion King

Based on the emulated genre matching, the most similar movie to the given references is option (C): The Lion King.

