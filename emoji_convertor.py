# a program to take typed emoji description and convert to emoji

import emoji

def main():

    string = input("Input: ")

    convert_emoji(string)

def convert_emoji(words):

    # split string into separate list of variables
    words = words.split()

    # for each variable in string check if starts and ends with : and if so turn to emoji
    for i in range(len(words)):
        if words[i].startswith(":") and words[i].endswith(":"):
            words[i] = emoji.emojize(words[i], language="alias")

    # loop through list and print each word or emoji
    for word in words:
        print(word, end=" ")

if __name__ == "__main__":
    main()