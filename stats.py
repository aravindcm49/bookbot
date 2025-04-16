def get_num_words(txt):
    words = txt.split() 
    # print(f"{len(words)} words found in the document")
    return len(words)

def get_char_count(text):
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha(): 
            char_counts[char] = char_counts.get(char, 0) + 1
    # print(char_counts)
    return char_counts

def get_sorted_list(dict):
    sorted_counts = sorted(
    dict.items(),
        key=lambda item: item[1],
        reverse=True
    )
    str = ""
    for char, count in sorted_counts:
        str += (f"{char}: {count}\n")
    return str
def print_report(path, words, dict):
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
{get_sorted_list(dict)[:-2]}
============= END ===============
""")
