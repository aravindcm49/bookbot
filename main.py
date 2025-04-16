from stats import get_num_words, get_char_count, get_sorted_list, print_report
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = get_num_words(file_contents)
        dict = get_char_count(file_contents)
        # get_sorted_list(char_counts)
        print_report(filepath, words, dict)
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book_text(sys.argv[1])

main()