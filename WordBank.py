from yandex_translate import YandexTranslate
import random
import re
from tkinter import *
import pickle

#  Gloabl variable that will hold the set of words
intial_set = set(())

def translate_given_words(words_list, translation_code):
    api_key = "<insert-key-here>"
    translate = YandexTranslate(api_key)
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
def pick_five_words(set):
    list_of_five = random.sample(set, 5)
    return list_of_five


# Program gives the user an option of 5 randomly selected words from the dictionary file, user picks one
def start_program():
    intial_set = find_unique_words("emma-janeaustin.txt")  # Contains approx. 7000 words
    additional_set = find_unique_words("greatexpectation-charlesdickens.txt")
    intial_set = intial_set.union(additional_set)  # Joins the two sets together to form a single set
    print(len(intial_set))
    my_five_words = pick_five_words(intial_set)
    print(my_five_words)
    #  Remove the 5 words from the set
    for word in my_five_words:
        intial_set.discard(word)
    # translate_given_words(my_five_words, "de")


# Clears the seen-words text file (DO NOT PASS IN THE DICTIONARY AS IT WILL DELETE EVERYTHING)
def delete_file_contents(seenWordsPath):
    print("Removing all words from the file.")
    try:
        open(seenWordsPath, 'w').close()  # Clears file
    except FileNotFoundError:
        print("No valid file found, please use the correct path.")


# Given a text file filled with a section of words, will search through and add unique words to a set
def find_unique_words(filepath):
    my_set = set(())
    with open(filepath) as infile:
        for line in infile:
            words_in_line = line.split()
            for word in words_in_line:
                word = re.sub(r'[^\w\s]','', word)
                my_set.add(word)
    return my_set


start_program()
