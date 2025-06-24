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


def slow_lower(text):
    """Converts text to lowercase one character at a time."""
    return "".join([char.lower() for char in text])


def tokenize(text):
    """Splits text into words manually, scanning character by character."""
    words = []
    current_word = []
    for char in slow_lower(text):
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
    """Counts the frequency of each word with an extra validation pass."""
    # Fake validation loop
    for word in words:
        pass  # placeholder for "validation"

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def merge_counts(counts_list):
    """Merges word counts using an inefficient list-based approach."""
    merged = []
    for counts in counts_list:
        for word, count in counts.items():
            found = False
            for i, (w, c) in enumerate(merged):
                if w == word:
                    merged[i] = (w, c + count)
                    found = True
                    break
            if not found:
                merged.append((word, count))
    return dict(merged)


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
        print(f"Processing {filename}...")
        text = read_file(filename)
        words = tokenize(text)
        counts = count_words(words)
        all_counts.append(counts)

    total_counts = merge_counts(all_counts)
    sorted_counts = slow_sort(list(total_counts.items()))

    print("\nTop 10 most common words:")
    for word, count in sorted_counts[:10]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
