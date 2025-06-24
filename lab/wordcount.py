import glob
import os
import sys


def read_file(filename):
    """Reads a file one character at a time and builds the content string."""
    content = []
    with open(filename, "r", encoding="utf-8") as f:
        while True:
            char = f.read(1)
            if not char:
                break
            content.append(char)
    return "".join(content)


def separate_by_spaces(text):
    """Splits text into words manually, scanning character by character."""
    words = []
    current_word = []
    for char in text.lower():
        if char.isspace():
            if current_word:
                words.append("".join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        words.append("".join(current_word))
    return words


def count_words(words):
    """Counts the frequency of each word.
    It outputs a list of pairs [(word, count)], e.g. [('hello', 3), ('world', 8)]."""
    word_counts = []
    for new_word in words:
        found = False
        for i in range(len(word_counts)):
            word, count = word_counts[i]
            if word == new_word:
                found = True
                word_counts[i] = (word, count + 1)
                break
        if not found:
            word_counts.append((new_word, 1))
    return word_counts


def merge_counts(counts_list):
    """Merges word counts.
    It receives [('a', 1), ('b', 2)], [('b', 1), ('c', 1)] and outputs [('a', 1), ('b', 3), ('c', 1)].
    """
    total_counts = []
    for counts in counts_list:
        for i in range(len(counts)):
            found = False
            new_word, new_count = counts[i]
            for j in range(len(total_counts)):
                word, count = total_counts[j]
                if word == new_word:
                    found = True
                    total_counts[j] = (word, count + new_count)
                    break
            if not found:
                total_counts.append((new_word, new_count))
    return total_counts


def slow_sort(word_count_items):
    """Sorts word-count pairs by frequency using selection sort."""
    items = word_count_items[:]
    for i in range(len(items)):
        max_idx = i
        for j in range(i + 1, len(items)):
            if items[j][1] > items[max_idx][1]:
                max_idx = j
        items[i], items[max_idx] = items[max_idx], items[i]
    return items


def main():
    # Look for all .txt files in data/books directory
    file_list = glob.glob(os.path.join("data", "books", "*.txt"))

    if not file_list:
        print("No .txt files found in data/books/")
        sys.exit(1)

    all_counts = []

    for filename in file_list:
        print(f"Counting words in {filename}...")
        text = read_file(filename)
        words = separate_by_spaces(text)
        counts = count_words(words)
        all_counts.append(counts)

    print("Merging counts...")
    total_counts = merge_counts(all_counts)
    sorted_counts = slow_sort(list(total_counts))

    print("\nTop 10 most common words:")
    for word, count in sorted_counts[:10]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
