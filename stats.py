def word_separator(book_contend):
    words_list = book_contend.split()
    words_count = len(words_list)
    return words_count
def count_characters(words_count):
    counts = {}
    tiny = words_count.lower()
    for char in tiny:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
def create_sorted_report(counts):
    keys = []
    for word, number in counts.items():
        key = {"char": word, "num": number}
        keys.append(key)
    keys.sort(key=sort_on, reverse=True)
    return keys
def sort_on(d):
    return d["num"]