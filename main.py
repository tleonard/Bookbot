def count_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict={
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
        'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 
        'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 
        'z': 0, ' ':0}
    char_text=text.lower()
    for i in char_text:
        if i in char_dict:
            char_dict[i] += 1
    return char_dict


def main ():
    book="books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        char_count_dict = get_char_count(file_contents)
        print(f"--- Begin report of {book} ---")
        print(f"{num_words} words found in the document")
        for i in char_count_dict:
            if i != ' ':
                print(f"The '{i}' character was found {char_count_dict[i]} times")
        #print(char_count_dict)

main()