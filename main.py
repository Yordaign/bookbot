def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(num_words)














def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()






















  #  with open("books/frankenstein.txt") as f:
  #      file_contents = f.read()
  #  print(file_contents)
#def word_count():
#    with open("books/frankenstein.txt") as f:
 #       file_contents = f.read()
 #       words = file_contents.split()
 #       count = len(words)
 #       print(count)
#if __name__ == "__main__":
   # main()
 #   word_count()