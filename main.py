from stats import word_separator, count_characters, create_sorted_report

def get_book_text(books_path):
    with open(books_path) as f:
        read_book = f.read()
    return read_book
def main():
    path = "books/frankenstein.txt"
    book_contend = get_book_text(path)
    words_counted = word_separator(book_contend)
    characters = count_characters(book_contend)
    ordered = create_sorted_report(characters)
    print(f"""
        ============ BOOKBOT ============
        Analyzing book found at books/frankenstein.txt...
        ----------- Word Count ----------
        Found {words_counted} words in total
        --------- Character Count -------
        print(f"Total letter count is {characters}""")
    
main()