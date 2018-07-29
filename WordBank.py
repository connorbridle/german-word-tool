from yandex_translate import YandexTranslate
import random
from tkinter import *


def translate_given_words(words_list, translation_code):
    translate = YandexTranslate("trnsl.1.1.20180729T203420Z.82690e64023c6383.3465f275a4cdf726ca3da96a18a3fc92fd40bb59")
    print("Languages: ", translate.langs)
    print("Translate: ", translate.translate("Bread", translation_code))
    for word in words_list:
        print("Translation: ", translate.translate(word, translation_code))


# Reading from the dictionary file
def read_from_dictionary(filepath):
    lines = open(filepath).read().splitlines()
    return lines


# Adds the words to another txt document which acts as a dictionary of learnt words
def mark_words_as_seen():
    print("Marking words as seen")

    # Appends the seen words to the text file
    with open('seen-words.txt', 'a') as myfile:
        myfile.write("Appended text")


# Resets all words back to the main dictionary
def reset_dictionary(dictionaryPath, seenWordsPath):
    print("Starting dictionary reset.")

    # Adds adds all of the words in the seenWords file back to the original dictionary
    delete_file_contents("SEENWORDSPATH")


# Picks 5 random numbers from the list of words for the user to learn
def pick_five_words():
    dict_of_words = read_from_dictionary("words.txt")
    list_of_five = []
    for x in range(5):
        list_of_five.append(dict_of_words[random.randint(0, len(dict_of_words))])
    return list_of_five


# Program gives the user an option of 5 randomly selected words from the dictionary file, user picks one
def start_program():
    my_five_words = pick_five_words()
    print(my_five_words)
    translate_given_words(my_five_words, "de")


# Clears the seen-words text file (DO NOT PASS IN THE DICTIONARY AS IT WILL DELETE EVERYTHING)
def delete_file_contents(seenWordsPath):
    print("Removing all words from the file.")
    try:
        open(seenWordsPath, 'w').close()  # Clears file
    except FileNotFoundError:
        print("No valid file found, please use the correct path.")


start_program()


