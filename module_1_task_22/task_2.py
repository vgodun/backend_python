def count_words_in_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"The file contains {word_count} words.")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")

if __name__ == "__main__":
    count_words_in_file("sample.txt")
