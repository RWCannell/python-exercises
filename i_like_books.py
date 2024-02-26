# Instructions for Assessment

# Open the text file 'files/i_like_books.txt' and write some Python code to determine the following:

# 1) How many times does the string 'book' appear in the text?
# 2) Which of the following authors are mentioned in the text file: Dostoevsky, 
#    Tolstoy, Hardy, Austen, Gaskell, Dumas? The output may be a list or a tuple.
# 3) Output a list of strings that are inside double quotation marks (you may use regex).
# 4) Altogether, how many non-empty lines does the text file have?

# 1) function for getting the number of occurrences of the string 'book'
def get_number_of_book_occurrences():
    text_file = open("files/i_like_books.txt", "r")
    text_as_string = text_file.read()
    occurrences_of_book = text_as_string.count("book")
    total_number_of_occurrences = occurrences_of_book
    text_file.close()
    return total_number_of_occurrences

# 2) function for creating a list of authors mentioned in the text file
def get_listed_authors():
    text_file = open("files/i_like_books.txt", "r")
    text_as_string = text_file.read()
    authors = [
        'Dostoevsky',
        'Tolstoy',
        'Hardy',
        'Austen',
        'Gaskell',
        'Dumas'
    ]
    mentioned_authors = []

    for author in authors:
        if author in text_as_string:
            mentioned_authors.append(author)
    text_file.close()
    return mentioned_authors

# 3) function for creating a list of strings contained inside double quotes
def get_strings_in_double_quotes():
    text_file = open("files/i_like_books.txt", "r")
    text_as_string = text_file.read()
    strings_in_double_quotes = []

    # brute-force solution using .split()
    split_by_double_quotes = text_as_string.split('\"')
    # since text in double quotes must have opening and closing tag, only take alternate (odd index) entries of split list
    for i in range(len(split_by_double_quotes)):
        if i % 2 == 1:
            strings_in_double_quotes.append(split_by_double_quotes[i])

    text_file.close()
    return strings_in_double_quotes

    # # using regex
    # import re
    # strings_in_double_quotes = re.findall(r'"([^"]*)"', text_as_string)
    # return strings_in_double_quotes

# 4) function for getting number of lines in text file
def get_number_of_non_empty_lines_in_file():
    text_file = open("files/i_like_books.txt", "r")
    count = 0
    for line in text_file:
        if line != "\n":
            count += 1

    text_file.close()
    return count

if __name__ == '__main__':
    # Solution to exercise 1
    total_number_of_occurrences_of_book = get_number_of_book_occurrences()
    print(f"1) Total number of occurrences of 'book': {total_number_of_occurrences_of_book}")

    # Solution to exercise 2
    listed_authors = get_listed_authors()
    print(f"2) List of authors: {listed_authors}")

    # Solution to exercise 3
    text_in_double_quotes = get_strings_in_double_quotes()
    print(f"3) List of text in double quotes: {text_in_double_quotes}")

    # Solution to exercise 4
    total_number_of_non_empty_lines = get_number_of_non_empty_lines_in_file()
    print(f"4) Total number of non-empty lines in file: {total_number_of_non_empty_lines}")