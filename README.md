# Finnish Practice

A command-line flashcard game for practising Finnish vocabulary, built with Python and SQLite.

## Features

- Vocabulary is stored in a SQLite database (`Flashcards.db`), created automatically on first run
- Words are grouped into 4 chapters (greetings, numbers, food, verbs)
- Translates English → Finnish: the program shows an English word and checks your answer
- Answers are not case-sensitive and extra spaces are ignored
- Shows the correct answer when you are wrong
- Type `exit` at the chapter menu to quit

## Requirements

- Python 3.x (SQLite is included in Python's standard library)

## How to run

```bash
git clone https://github.com/iamozansson/Finnish-Practice.git
cd Finnish-Practice
python3 Python-Finnish-Study.py
```

## Example

```
Welcome to the Finnish practice game!
Please select chapters 1-4 to practise
1
You have choosen Chapter 1, let's start!
What is Finnish translation of 'Hello'
Your answer = terve
Correct answer!
```

## How it works

- A `Flashcards` table stores `id`, `chapter`, `english` and `finnish`
- `INSERT OR IGNORE` with a `UNIQUE` constraint on the English word prevents duplicates when the script runs again
- Queries use parameterized statements (`?`) instead of string formatting

## What I practised

- Working with SQLite from Python (`sqlite3`)
- Creating tables and inserting data
- Loops, input handling and validation
- Writing a small interactive CLI program
