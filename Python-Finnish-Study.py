import sqlite3

conn = sqlite3.connect("Flashcards.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Flashcards(
               id INTEGER PRIMARY KEY,
               chapter INTEGER NOT NULL,
               english TEXT UNIQUE NOT NULL,
               finnish TEXT NOT NULL
               )
""")
words = [
    (1, "Hello", "Terve"),
    (1, "Hi", "Moi"),
    (2, "One", "Yksi"),
    (2, "Two", "Kaksi"),
    (2, "Three", "Kolme"),
    (3, "Apple", "Omena"),
    (3, "Banana", "Banani"),
    (3, "Potato", "Peruna"),
    (4, "Run", "Juosta"),
    (4, "Swim", "Uida"),
    (4, "Speak", "Puhua"),
    (4, "Go", "Mennä"),
    (4, "Come", "Tulla")

]

for chapter, english, finnish in words:
    cursor.execute("INSERT OR IGNORE INTO Flashcards (chapter, english, finnish) VALUES (?, ?, ?)",
                   (chapter, english, finnish))

conn.commit()

cursor.execute("SELECT * FROM Flashcards")
rows = cursor.fetchall()
print(rows)


while True:
    print("Welcome to the Finnish practice game!\nPlease select chapters 1-4 to practise")
    baslik = input("")

    if baslik.lower() == 'exit':
        print("Thank you for using this program! See you next time!")
        break

    if baslik in ['1', '2', '3', '4']:
        chapter_num = int(baslik) 
        print(f"You have choosen Chapter {chapter_num}, let's start!")
        cursor.execute("Select english, finnish FROM Flashcards WHERE chapter = ?", (chapter_num,))
        rows = cursor.fetchall()
        if not rows:
            print("There is no such chapter.")
            continue

        for english, finnish in rows:
            print(f"What is Finnish translation of '{english}'")
            answer = input("Your answer = ")
            if answer.strip().lower() == finnish.lower():
                print("Correct answer!")
            else:
                print(f"Unfortunately, wrong answer! Correct answer should be: {finnish}")

        change_chapter = input("Would you like to change the chapter? (y)/(n)").lower()

        if change_chapter != 'y':
            print("Thank you for using this program! See you next time!")
            break        