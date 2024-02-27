# Instructions for Assessment

# Open the text file 'files/i_like_books.txt' and write some Python code to determine the following:

# 1) How many times does the string 'book' appear in the text?
# 2) Which of the following authors are mentioned in the text file: ['Dostoevsky', 
#    'Tolstoy', 'Hardy', 'Austen', 'Gaskell', 'Dumas']? The output may be a list or a tuple.
# 3) Output a list of strings that are inside double quotation marks (you may use regex).
# 4) Altogether, how many non-empty lines does the text file have?
# 5) Reverse the following list of authors: ['Dostoevsky', 
#    'Tolstoy', 'Hardy', 'Austen', 'Gaskell', 'Dumas']?

# 1) function for getting the number of occurrences of the string 'book'
def get_number_of_book_occurrences():
    # to open a file and store it as a variable, use 'text_file = open("/path/to/file", "r")'
    # the text file can be converted to a string with 'text_as_string = text_file.read()'

    # your code over here
    return

# 2) function for creating a list of authors mentioned in the text file
def get_listed_authors():
    # your code over here
    return

# 3) function for creating a list of strings contained inside double quotes
def get_strings_in_double_quotes():
    # your code over here

    # Hint: if you choose to use regex, remember to import the regex library, 'import re'
    # Here is some useful information:
    # re.findall(r'"put condition inside here"', string) returns a list containing all matches of given condition
    # [] a set of characters
    # ^  starts with
    # $  ends with
    # \  used to escape special characters
    # *  zero or more occurrences
    # +  one or more occurrences
    # ?  zero or one occurrences
    #
    # You don't HAVE TO use regex, you can iterate over the text file and use old-fashioned logic
    return

# 4) function for getting number of lines in text file
def get_number_of_non_empty_lines_in_file():
    # your code over here
    # Hint: an empty line can be identified by "\n"
    return

# 5) function for reversing elements in a list
def reverse_list_of_authors():
    authors = [
        'Dostoevsky',
        'Tolstoy',
        'Hardy',
        'Austen',
        'Gaskell',
        'Dumas'
    ]
    # your code over here
    return authors

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

    # Solution to exercise 5
    reversed_list_of_authors = reverse_list_of_authors()
    print(f"5) Reversed list of authors: {reversed_list_of_authors}")

# To run the code, open a terminal and run the command:
# python3 i_like_books_exercise.py (or python i_like_books_exercise.py if using python v2)