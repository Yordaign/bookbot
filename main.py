def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_char(text)
    print(get_report(character_count, num_words, book_path))

#currently coding the below: need to add a sort function to the list of dictionaries, and integrate them into the final report string <3
#you got this king

def sort_on(dict):
    return dict["num"]

def get_report(char_dict, num_words, book_path):
    report = f"--- Begin report of {book_path} ---\n"
    report += f"{num_words} words found in the document \n\n"
    char_dict_list = [{"char": char, "num": count} for char, count in char_dict.items() if char.isalpha()]
    char_dict_list.sort(reverse=True, key=sort_on)
    for entry in char_dict_list:
        report += f"The '{entry['char']}' character was found {entry['num']} times\n"
    report += "--- End report ---"
    return report

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