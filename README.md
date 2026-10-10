# Finnish Practice

A command-line flashcard game for practising Finnish vocabulary, built with Python and SQLite.

## Features

- Stores vocabulary in a SQLite database (`Flashcards.db`)
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

The `Flashcards.db` file must exist on the host before running the following command. You can create it by running the application locally first.

```bash
docker run -it --rm \
  --mount type=bind,source="$(pwd)/Flashcards.db",target=/app/Flashcards.db \
  finnish-practice
```

The bind mount connects the database file on the host to `/app/Flashcards.db` inside the container. Changes written to the database remain available on the host after the container is removed.

### Docker options

- `-it`: Runs the application interactively in the terminal
- `--rm`: Removes the container when it exits
- `--mount`: Mounts the host database file into the container

## Example

```text
Welcome to the Finnish practice game!
Please select chapters 1-4 to practise
```

## How it works

- The `Flashcards` table stores `id`, `chapter`, `english`, and `finnish`.
- The `english` column has a `UNIQUE` constraint, which prevents duplicate English entries.
- `INSERT OR IGNORE` skips inserting a row when it violates a constraint, such as the `UNIQUE` constraint.
- Parameterized SQL queries (`?`) are used instead of string formatting.

## What I practised

- Working with SQLite from Python (`sqlite3`)
- Creating tables and inserting data
- Loops, input handling, and validation
- Building an interactive command-line application
- Creating a Docker image and running a container
- Using bind mounts to persist database changes on the host
