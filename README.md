# Finnish Practice

A command-line flashcard game for practising Finnish vocabulary, built with Python and SQLite.

## Features

- Stores vocabulary in a SQLite database (`Flashcards.db`), created automatically on the first run
- Organizes words into four chapters: greetings, numbers, food, and verbs
- Practices English-to-Finnish translations
- Accepts answers regardless of letter case and ignores extra spaces
- Shows the correct translation when an answer is incorrect
- Allows users to type `exit` at the chapter menu to quit

## Technologies

- Python 3
- SQLite
- Docker

## Quick start with Docker

```bash
git clone https://github.com/iamozansson/Finnish-Practice.git
cd Finnish-Practice
docker build -t finnish-practice .
docker run -it --rm finnish-practice
```

The application creates the database and inserts the vocabulary on the first run, so no extra setup is needed.

## How to run locally

### Requirements

- Python 3.x (SQLite is included in Python's standard library)

Clone the repository and run the application:

```bash
git clone https://github.com/iamozansson/Finnish-Practice.git
cd Finnish-Practice
python3 Python-Finnish-Study.py
```

The application creates the `Flashcards` table if it does not exist and inserts the predefined vocabulary into the database.

## How to run with Docker

### Requirements

- Docker installed and running

Build the Docker image from the project directory:

```bash
docker build -t finnish-practice .
```

### Run with a persistent database

The database file is not stored in the repository (it is listed in `.gitignore`). Create an empty file on the host first. The application initialises it on the first run:

```bash
touch Flashcards.db
docker run -it --rm \
  --mount type=bind,source="$(pwd)/Flashcards.db",target=/app/Flashcards.db \
  finnish-practice
```

The bind mount connects the database file on the host to `/app/Flashcards.db` inside the container. Data written to the database stays on the host after the container is removed.

### Docker options

- `-it`: Runs the application interactively in the terminal
- `--rm`: Removes the container when it exits
- `--mount`: Mounts the host database file into the container

## Example

```text
Welcome to the Finnish practice game!
Please select chapters 1-4 to practise
1
You have chosen Chapter 1, let's start!
What is Finnish translation of 'Hello'
Your answer = terve
Correct answer!
```

## How it works

- The `Flashcards` table stores `id`, `chapter`, `english`, and `finnish`.
- The `english` column has a `UNIQUE` constraint, which prevents duplicate English entries.
- `INSERT OR IGNORE` skips inserting a row when it violates a constraint, such as the `UNIQUE` constraint.
- Parameterized SQL queries (`?`) are used instead of string formatting.
- The database file is created on the first run and is not tracked by Git.

## Planned features

- Progress tracking: store each answer in a separate table and show which words need more practice

## What I practised

- Working with SQLite from Python (`sqlite3`)
- Creating tables and inserting data
- Loops, input handling, and validation
- Building an interactive command-line application
- Creating a Docker image and running a container
- Using bind mounts to persist database changes on the host