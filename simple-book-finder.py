myBooks = [
    "Harry Potter and the Philosopher's Stone",
    "Harry Potter and the Chamber of Secrets",
    "A Game of Thrones",
    "A Clash of Kings",
    "Great Expectations",
    "Oliver Twist",
    "Northanger Abbey",
    "Othello",
    "King Lear",
    "Matilda",
    "James and the Giant Peach",
    "The Count of Monte Cristo",
    "Crime and Punishment",
    "The Brothers Karamazov",
    "The Idiot",
    "The Pillars of the Earth",
    "Sapiens: A Brief History of Humankind"
]

requestedBook = input('Which book would you like to read? ')

found = False

for book in myBooks:
    if requestedBook.lower() == book.lower():
        found = True
        break

if found:
    print("Yes, we have " + "'" + requestedBook + "'. We hope you enjoy reading it!")
else:
    print("Sadly, we do not have a book called " + "'" + requestedBook + "'.")
