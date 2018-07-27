

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


# Program gives the user an option of 5 randomly selected words from the dictionary file, user picks one
def start_program():
    print("")


# Clears the seen-words text file (DO NOT PASS IN THE DICTIONARY AS IT WILL DELETE EVERYTHING)
def delete_file_contents(seenWordsPath):
    print("Removing all words from the file.")
    try:
        open(seenWordsPath, 'w').close()  # Clears file
    except FileNotFoundError:
        print("No valid file found, please use the correct path.")


filename = 'words.txt'
myWords = read_from_dictionary(filename)
print("Words loaded, Initialising program.")

