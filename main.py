import sys
from stats import word_separator, count_characters, create_sorted_report

def get_book_text(books_path):
    with open(books_path) as f:
        read_book = f.read()
    return read_book
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    book_contend = get_book_text(path)
    words_counted = word_separator(book_contend)
    characters = count_characters(book_contend)
    ordered = create_sorted_report(characters)
    
    # ÁREA DE PRINT:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {words_counted} total words")
    print("--------- Character Count -------")
    for item in ordered:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]} ")
    print("============= END ===============")
main()