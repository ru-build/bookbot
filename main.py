def get_book_text(books_path):
    with open(books_path) as f:
        read_book = f.read()
    return read_book
def main():
    path = "books/frankenstein.txt"
    book_contend = get_book_text(path)
    print(book_contend)
def word_separator(book_contend):
    words_list = book_contend.split()
    words_count = words_list.len()
    return words_count
main()