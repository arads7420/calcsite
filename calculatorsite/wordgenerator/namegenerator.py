from PyDictionary import PyDictionary
import random 
import math
import json

dictionary = PyDictionary()


#Unwanted characters
bad_char_list = ['.', ',', '=', '/', '\\', '-', '*',  '$', '#', '^', '!', ')', '(', '{', '}', '[', ']', '`', '~', '<', '>']

def sanitize_word(word):
    for symbol in bad_char_list:
        word = word.replace(symbol, '')
    return word

#Takes as input: A word list, No.of words required
def gen_random_names(words, n):
    #Find related words
    related_words = []
    for word in words:
        if(dictionary.synonym(word)):
            related_words = related_words + dictionary.synonym(word)

    word_list = list(open(r"D:\Programming Projects\WebDevelopment\Django Random Word\calculatorsite\wordgenerator\wordgen_lists\word_list.txt", "r"))
    if related_words:
        word_list = word_list + related_words

    bad_word_list = list(open(r"D:\Programming Projects\WebDevelopment\Django Random Word\calculatorsite\wordgenerator\wordgen_lists\badwords.txt", "r"))

    response_words = []
    #Generate random names
    for _ in range(0, n):
        first_part = str(words[random.randint(0, len(words) - 1)]).strip('\n').capitalize()
        second_part = str(word_list[random.randint(0, len(word_list) - 1)]).strip('\n').capitalize()
        while(second_part.lower() in bad_word_list or len(second_part) > 7):
            second_part = str(word_list[random.randint(0, len(word_list) - 1)]).strip('\n').capitalize()

        second_part = sanitize_word(second_part)

        generated_word_1 = first_part + " " + second_part
        generated_word_2 = second_part + " " + first_part
        generated_word_3 = first_part + second_part
        generated_word_4 = second_part + first_part

        generated_words = [generated_word_1, generated_word_2, generated_word_3, generated_word_4]
        final_word = random.choice(generated_words).strip(" ")
        response_words.append(final_word)
    return response_words