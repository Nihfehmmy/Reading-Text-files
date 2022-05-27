# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from fileinput import filename
from itertools import count
import string


def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename, "r")
    lines = file.readlines()
    return lines
    print(read_file_content(filename))


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count = dict ()
    for line in text:
        line = line.strip()
        for character in string.punctuation:
            line = line.replace(character, "")
            line = line.lower()
            words = line.split(" ")

        for word in words:
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

        for key in list(count.keys()):
            print(key, ":", count[key])
count_words()