def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_char(text)












def count_char(text):
    char_dict = {}
    lower = text.lower()
    for i in lower:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    return char_dict

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