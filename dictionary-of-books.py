dictionaryOfBooksAndAuthors = {
    "Harry Potter and the Philosopher's Stone": "J. K. Rowling",
    "Harry Potter and the Chamber of Secrets": "J. K. Rowling",
    "Harry Potter and the Prisoner of Azkaban": "J. K. Rowling",
    "Harry Potter and the Goblet of Fire": "J. K. Rowling",
    "Harry Potter and the Order of the Phoenix": "J. K. Rowling",
    "Harry Potter and the Half Blood Prince": "J. K. Rowling",
    "Harry Potter and the Deathly Hallows": "J. K. Rowling",
    "A Game of Thrones": "George R. R. Martin",
    "A Clash of Kings": "George R. R. Martin",
    "A Storm of Swords": "George R. R. Martin",
    "Great Expectations": "Charles Dickens",
    "Oliver Twist": "Charles Dickens",
    "Hard Times": "Charles Dickens",
    "Nicholas Nickleby": "Charles Dickens",
    "Northanger Abbey": "Jane Austen",
    "Othello": "William Shakespeare",
    "King Lear": "William Shakespeare",
    "Macbeth": "William Shakespeare",
    "Hamlet": "William Shakespeare",
    "Midsummer Night's Dream": "William Shakespeare",
    "Matilda": "Roald Dahl",
    "James and the Giant Peach": "Roald Dahl",
    "Fantastic Mr Fox": "Roald Dahl",
    "The Witches": "Roald Dahl",
    "Charlie and the Chocolate Factory": "Roald Dahl",
    "The Count of Monte Cristo": "Alexandre Dumas",
    "Crime and Punishment": "Fyodor Dostoevsky",
    "The Brothers Karamazov": "Fyodor Dostoevsky",
    "The Idiot": "Fyodor Dostoevsky",
    "The Pillars of the Earth": "Ken Follett",
    "Sapiens: A Brief History of Humankind": "Yuval Noah Harari"
}

# Our goal is to find out how many books of each author we own. There exist many built-in Python dictionary methods
# which would make this task quite easy. However, we'd like to go through the logic more slowly.

# One way to do this would be to create a new dictionary where the authors are the 'keys' and the 'values' are the number
# of books. Let's try that first.
dictionaryOfAuthorsAndNumberOfBooks = {}
listOfAuthors = list(dictionaryOfBooksAndAuthors.values())

# The listOfAuthors returns duplicates. We don't want that, so we convert the list into a set. Sets remove duplicates.
setOfAuthors = set(listOfAuthors)

# Now we can initialise a new dictionary where the author is the key and all the initial values are 0.
dictionaryOfAuthorsAndNumberOfBooks = {numOfBooks: 0 for numOfBooks in setOfAuthors}

# Now we will iterate over the values of the original dictionary (where there are duplicates), and count the number of duplicates
# of each author. These values will be added to the new dictionary.
for value in dictionaryOfBooksAndAuthors.values():
    if value in dictionaryOfBooksAndAuthors.values():
        dictionaryOfAuthorsAndNumberOfBooks[value] += 1
    else:
        dictionaryOfAuthorsAndNumberOfBooks[value] = 1

# Our dictionary should look something like this:
"""
{
'Ken Follett': 1, 
'Roald Dahl': 5, 
'Charles Dickens': 4, 
'J. K. Rowling': 7, 
'Jane Austen': 1, 
'Alexandre Dumas': 1, 
'Fyodor Dostoevsky': 3, 
'George R. R. Martin': 3, 
'Yuval Noah Harari': 1, 
'William Shakespeare': 5
}
"""

# Finally, we'll print out the author and number of books.
for key, value in dictionaryOfAuthorsAndNumberOfBooks.items():
    print("We own " + str(value) + " book(s) by author " + key + ".\n")
